import rpa as r

r.init(visual_automation = True)
r.url('https://www.google.com/')
r.type('//*[@name="q"]', 'hello world')
r.snap('page', 'results.png')
r.close()