"""Synthetic resource edges; no chapter, cultural fact or external path is loaded."""
import copy,json
def resource_controls(history,profile):
 def request(h,p=None):return {'operation':'compare'if p is not None else'validate','history_json':json.dumps(h,separators=(',',':')),'profile_json':None if p is None else json.dumps(p,separators=(',',':'))}
 maximum={'people_id':'maximum','title':'Synthetic resource maximum','worldview':'x'*4096,'framing_notes':['demo note']*128,'source_story_refs':[{'path':'synthetic/s.md'}for _ in range(256)],'eras':[]}
 for era in range(32):
  maximum['eras'].append({'era_id':f'era-{era}','title':'Demo era','persons':[{'person_id':f'p{era*8+i}','display_name':'P','role':'r','source_story_refs':[{'path':'synthetic/s.md'}]}for i in range(8)],'events':[{'event_id':f'e{era*16+i}','era_id':f'era-{era}','title':'E','event_kind':'test','consequence':'Supplied claim','actors':['p0','p1','p2','p3'],'places':['a','b','c','d'],'source_story_refs':[{'path':'synthetic/s.md'}for _ in range(3)]}for i in range(16)]})
 pmax={'profile_id':'x'*4096,'required_event_ids':[f'e{i}'for i in range(512)],'required_person_ids':[f'p{i%256}'for i in range(512)],'required_story_paths':['synthetic/s.md']*512,'forbidden_external_framings':[f'not-present-{i}'for i in range(128)]}
 def control(name,value,expected):return {'name':name,'request':value,'expected_kind':expected}
 result=[control('combined-admitted-maximum',request(maximum,pmax),'report')];assert len(result[0]['request']['history_json'].encode())<=262144 and len(result[0]['request']['profile_json'].encode())<=131072
 for name,modify in [
  ('eras',lambda h:h['eras'].append({'era_id':'extra','title':'Extra'})),
  ('persons',lambda h:h['eras'][0]['persons'].append(copy.deepcopy(h['eras'][0]['persons'][0]))),
  ('events',lambda h:h['eras'][0]['events'].append(copy.deepcopy(h['eras'][0]['events'][0]))),
  ('references',lambda h:h['source_story_refs'].append({'path':'synthetic/s.md'})),
  ('actors_places',lambda h:h['eras'][0]['events'][0]['actors'].append('p0')),
  ('framing_notes',lambda h:h['framing_notes'].append('extra')),
  ('string',lambda h:h.update(worldview='x'*4097))]:
  h=copy.deepcopy(maximum);modify(h);result.append(control('history-over-'+name,request(h,pmax),'browser_refusal'))
 for field,value in [('required_event_ids','e0'),('required_person_ids','p0'),('required_story_paths','synthetic/s.md'),('forbidden_external_framings','extra')]:
  p=copy.deepcopy(pmax);p[field].append(value);result.append(control('profile-over-'+field,request(maximum,p),'browser_refusal'))
 for count in [1024,1025]:
  expected='report'if count==1024 else'browser_refusal'
  h=copy.deepcopy(history);h.update({f'extension_{i}':0 for i in range(count)});result.append(control(f'ignored-history-{count}',request(h),expected))
  p=copy.deepcopy(profile);p.update({f'extension_{i}':0 for i in range(count)});result.append(control(f'ignored-profile-{count}',request(history,p),expected))
 return result
