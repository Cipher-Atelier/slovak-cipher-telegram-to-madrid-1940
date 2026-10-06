#!/usr/bin/env python3
"""New, read-only replay audit. Does not re-fit keys or certify manuscript truth.
Run from this reading packet: python3 replay.py
"""
from pathlib import Path
import json,csv,hashlib,re,string,sys
P=Path(__file__).resolve().parent
E=P/'evidence' if (P/'evidence').exists() else P/'repro_inventory_core'
REPORT={}
def txt(p):return p.read_text(encoding='utf-8')
def js(p):return json.loads(txt(p))
def sha(b):return hashlib.sha256(b).hexdigest()
def record(topic,**kw):REPORT[topic]={'status':'PASS','scope':'mechanical replay only',**kw}

if sys.flags.optimize:
 raise SystemExit('Run normal Python; assertion checks must remain enabled.')

# Madrid: retain the consumed first test and post-test source correction separately.
q=E/'Madrid1940_Forward_Evidence/mzv_c1940/pilot_v4/forward_diagnostic';fixed=js(q/'FROZEN_SELECTED_KEY.json');key=dict(zip(string.ascii_lowercase,fixed['selected']['key']));first=js(q/'HELDOUT_FIRST_EVALUATION.json');post=js(q/'HELDOUT_POST_SOURCE_AUDIT.json')
decode=lambda c:''.join(key.get(x,'?') for x in c)
assert decode(first['ciphertext'])==first['literal_frozen_key_plaintext'];assert decode(post['preferred_cipher'])==post['preferred_plaintext']
counts=js(q/'KEY_SUPPORT_COUNTS.json');assert ''.join(r['cipher'] for r in counts if r['training_occurrences']==0)=='cfhq'
train=txt(q/'target_training_adapter.txt').strip();assert decode(train[::-1])==fixed['selected']['plaintext_training_logical']  # archived solver adapter is reversed; logical experiment is forward
record('madrid-1940',first_literal=first['literal_frozen_key_plaintext'],post_source_literal=post['preferred_plaintext'],solver_adapter_positions=len(train),declared_training_span=77,heldout_masks=20,singleton_mappings=[r['cipher'] for r in counts if r['training_occurrences']==1],untrained_mappings='cfhq')

print(json.dumps(REPORT,ensure_ascii=False,indent=2))
