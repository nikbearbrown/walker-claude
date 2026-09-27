"""lock: pad measured Kokoro mp3 to frame, limit to -1.5 dBTP into audio/<id>-lim.wav (outro +1.0 s tail).
cues: bind GodotDesignBoard card cues to spoken phrases via mp3/words.json (align.py)."""
import argparse, json, math, re, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; SHEET=ROOT/'beat_sheet.json'; FPS=30
def probe(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',str(p)],text=True))
def load(): return json.loads(SHEET.read_text())
def save(s): SHEET.write_text(json.dumps(s,indent=1)+'\n')
def lock():
    s=load(); (ROOT/'audio').mkdir(exist_ok=True)
    for b in s['beats']:
        bid=b['beat_id']; src=ROOT/'mp3'/f'beat-{bid}.mp3'; assert src.exists(), f'missing {src}'
        lead=float(b.get('lead_silence_s',0)); tail=1.0 if b.get('kind')=='outro_voice' else 0.3
        nar=probe(src); d=math.ceil((nar+lead+tail)*FPS)/FPS; dst=ROOT/'audio'/f'{bid}-lim.wav'
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(src),'-af',f'adelay={round(lead*1000)}:all=1,apad,aresample=48000,alimiter=limit=0.841:attack=5:release=50:level=false','-t',str(d),'-ar','48000','-ac','2','-c:a','pcm_s16le',str(dst)],check=True)
        b.update(audio_file=f'audio/{bid}-lim.wav',actual_duration_s=d,narration_duration_s=round(nar,3))
        if b.get('kind')=='outro_voice': b['hold_note']=f'spoken outro {nar:.2f}s + 1.0s silent tail; no jingle (OUTRO-LOCK)'
        b['shot']['remotion']['props']['durationSeconds']=d
    s['metadata']['audio_locked']=True; s['metadata']['duration_s']=round(sum(b['actual_duration_s'] for b in s['beats']),3); save(s)
    print('AUDIO LOCKED',s['metadata']['duration_s'],'s')
def cues():
    s=load(); words=json.loads((ROOT/'mp3/words.json').read_text()); fps=words['fps']; norm=lambda t:re.sub('[^a-z0-9]','',t.lower()); report=[]
    for b in s['beats']:
        if not b.get('cue_phrases'): continue
        toks=words['beats'][b['beat_id']]; out=[]; n=len(b['cue_phrases']); dur=b['actual_duration_s']
        for k,c in enumerate(b['cue_phrases']):
            target=[norm(w) for w in c['phrase'].split() if norm(w)]
            hits=[i for i in range(len(toks)) if [norm(t['text']) for t in toks[i:i+len(target)]]==target]
            if hits: at=toks[hits[0]]['startFrame']/fps+float(b.get('lead_silence_s',0)); how='matched'
            else: at=round(dur*(k+0.5)/n,2); how='UNMATCHED, evenly spaced'
            out.append({'at':round(at,2),'card':c['card']}); report.append({'beat':b['beat_id'],'phrase':c['phrase'],'at':round(at,2),'how':how})
        b['shot']['remotion']['props']['cues']=sorted(out,key=lambda x:x['at'])
    save(s); (ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence/cue-timing.json').write_text(json.dumps({'method':'known narration words aligned by faster-whisper (align.py); unmatched phrases spaced evenly and reported','rows':report},indent=1))
    print('\n'.join(f"{r['beat']} {r['at']:6.2f} {r['how']}: {r['phrase']}" for r in report))
if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('task',choices=['lock','cues']); a=ap.parse_args(); {'lock':lock,'cues':cues}[a.task]()
