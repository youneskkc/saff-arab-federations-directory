import csv, html, json, os
rows = [
('إتحاد الجامعات العربية','https://www.aaru.edu.jo/','','لم يُعثر عليه'),
('إتحاد المحامين العرب','https://www.alu1944.org/','','لم يُعثر عليه'),
('إتحاد قيادات المرأة العربية','https://www.arabwomenun.com/','','لم يُعثر عليه'),
('اتحاد الصيادلة العرب','https://www.apharmu.com/','','لم يُعثر عليه'),
('اتحاد الغرف العربية','https://uac-org.org/','','لم يُعثر عليه'),
('اتحاد المؤرخين العرب','http://arabhistoryso.net/','','لم يُعثر عليه'),
('اتحاد المبدعين العرب','https://www.arabcreators.org/','','لم يُعثر عليه'),
('اتحاد المصارف العربية','https://uabonline.org/','','https://uabonline.org/feed/'),
('اتحاد المقاولين العرب','http://www.fac-arab.com/','','لم يُعثر عليه'),
('اتحاد المهندسين الزراعيين العرب','https://aaunion.org/','','لم يُعثر عليه'),
('اتحاد الناشرين العرب','http://www.arab-pa.org/','','لم يُعثر عليه'),
('اتحاد رجال الأعمال العرب','http://fab-jo.org/','','http://fab-jo.org/?feed=rss2'),
('اتحاد المستثمرات العرب','https://awiu.net/','','لم يُعثر عليه'),
('الاتحاد العام العربي للتأمين','https://gaif-home.gaif.org/home','','لم يُعثر عليه'),
('الاتحاد العام للمنتجين العرب','http://www.mondialeg.tv/','','لم يُعثر عليه'),
('الاتحاد العربي للأسمدة','https://arabfertilizer.org/','','لم يُعثر عليه'),
('الاتحاد العربي للعمل التطوعي','https://affva.org/','https://www.facebook.com/AFFVA.ORG/','لم يُعثر عليه'),
('الاتحاد العربي للنقل الجوي','https://www.aaco.org/home','','لم يُعثر عليه'),
('الاتحاد العام للأدباء والكتاب العرب','','','لم يُعثر عليه'),
('الاتحاد العام للخبراء العرب','https://guae.org/','','لم يُعثر عليه'),
('الاتحاد العربي لتنمية الصادرات الصناعية','http://www.auied.com/','','لم يُعثر عليه'),
('الاتحاد العربي للصناعات الهندسية','http://arabindustries.org/','','لم يُعثر عليه'),
('الاتحاد العربي للمعارض والمؤتمرات','https://auiec.org/','','لم يُعثر عليه'),
('الاتحاد العربي لتنمية الصادرات والصناعات','','','لم يُعثر عليه'),
('الاتحاد العربي للإسمنت ومواد البناء','https://www.aucbm.net/','','لم يُعثر عليه'),
('الاتحاد العربي للاقتصاد الرقمي','https://arab-digital-economy.org/','','لم يُعثر عليه'),
('الاتحاد العربي للبناء والتنمية العقارية','https://www.credaunion.com/','','لم يُعثر عليه'),
('الاتحاد العربي للتطوع','https://arabvu.org/','','لم يُعثر عليه'),
('الاتحاد العربي للتنمية الاجتماعية','','','لم يُعثر عليه'),
('الاتحاد العربي للتنمية المستدامة والبيئة','https://www.ausde.org/','','لم يُعثر عليه'),
('الاتحاد العربي للصناعات الغذائية','https://www.arabffi.org/','','لم يُعثر عليه'),
('الاتحاد العربي للمخلصين الجمركيين','http://www.1auce.org/','','لم يُعثر عليه'),
('الاتحاد العربي لمكافحة التزوير والتزييف','https://aucfc.online/','','لم يُعثر عليه'),
('الاتحاد العربي لمنتجي الأسماك','http://kenanaonline.com/arabfish','','لم يُعثر عليه'),
('الاتحاد العربي لعلوم الفضاء والفلك','https://auass.com/','','لم يُعثر عليه'),
]
source='https://saffportal.org/saff_members_arabic-sitemap.xml'
with open('data.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f, lineterminator='\n'); w.writerow(['id','federation','official_website','social_media','rss_or_atom'])
    for i,r in enumerate(rows,1): w.writerow([i,*r])
def link(u): return f'[{u}]({u})' if u.startswith('http') else u
md=['# الاتحادات العربية المدرجة في saffportal.org','', '## دليل منظمات العمل العربي المشترك','', 'الدليل الموسع لمنظمات وهيئات العمل العربي المشترك منشور في [مستودع مستقل](https://github.com/youneskkc/arab-joint-action-organizations) وله [صفحة GitHub Pages](https://youneskkc.github.io/arab-joint-action-organizations/). يشمل الجهات التي ذكرها SAFF Portal وإضافات موثقة من مواقع رسمية ومصادر مؤسسية، تحت رخصة [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).','', f'> نسخة بحثية قابلة للاستشهاد، آخر تحقق: 2026-09-27. المصدر الأساسي: {source}','',f'**عدد السجلات: {len(rows)}**','', '| # | الاتحاد | الموقع المباشر | الشبكات الاجتماعية | RSS/Atom |','|---:|---|---|---|---|']
for i,(n,s,soc,feed) in enumerate(rows,1): md.append(f'| {i} | {n} | {link(s) if s else "غير مذكور"} | {link(soc) if soc else "لم يُعثر عليه"} | {link(feed) if feed.startswith("http") else feed} |')
md += ['', '## المنهجية', '', '1. استُخدمت خريطة موقع SAFF Portal الخاصة بنوع المحتوى `saff_members_arabic` كنقطة انطلاق لا كمصدر حصري، ثم استُكمل البحث في المواقع الرسمية والأدلة المؤسسية المستقلة.', '2. أُدرج الموقع الرسمي فقط بعد مراجعة الموقع المرشح والتحقق من صلته بالاتحاد من صفحاته الرسمية أو من مصادر مؤسسية مستقلة؛ لذلك قد تختلف درجة حداثة الروابط أو توفرها.', '3. استُخرجت الروابط الخارجية من صفحات الاتحادات، واستُبعدت روابط الحسابات العامة المتكررة الخاصة بالملتقى `SAFFPAGE` من عمود الشبكات الاجتماعية.', '4. أُدرج الموقع كرابط مباشر رئيسي، وليس كرابط دليل أو صفحة شبكة اجتماعية، ما لم يكن ذلك هو الحضور الرسمي الوحيد الموثق للجهة.', '5. فُحصت الصفحة الرئيسية للموقع والمسارات الشائعة للخلاصات (`/feed/` و`/rss.xml` و`/atom.xml` و`?feed=rss2`) بحثًا عن RSS أو Atom. عدم وجود رابط في الجدول يعني عدم العثور عليه أثناء الفحص، ولا يثبت استحالة وجوده خلف مسار آخر أو عبر واجهة ديناميكية.', '6. هذه القائمة تمثل ما أمكن التحقق منه حتى 2026-09-27، وقد تتغير مواقع الاتحادات أو روابطها لاحقًا.', '', '## مصادر', '', f'- [خريطة صفحات الاتحادات في SAFF Portal]({source})', '- [الموقع الرئيسي للملتقى](https://saffportal.org/)', '- [الموقع الرسمي للاتحاد العربي لعلوم الفضاء والفلك](https://auass.com/)', '', '## الترخيص', '', 'البيانات الوصفية والجدول منشوران لأغراض تعليمية وبحثية تحت رخصة [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). يرجى الاستشهاد بالمصدر الأصلي والتحقق من الروابط قبل الاستخدام الرسمي.']
open('README.md','w',encoding='utf-8').write('\n'.join(md)+'\n')
# simple static GitHub Pages
trs=[]
for i,(n,s,soc,feed) in enumerate(rows,1):
    def a(u): return f'<a href="{html.escape(u)}" rel="noopener">{html.escape(u)}</a>' if u.startswith('http') else html.escape(u)
    trs.append(f'<tr><td>{i}</td><td>{html.escape(n)}</td><td>{a(s) if s else "غير مذكور"}</td><td>{a(soc) if soc else "لم يُعثر عليه"}</td><td>{a(feed) if feed.startswith("http") else html.escape(feed)}</td></tr>')
page=f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>الاتحادات العربية | SAFF Portal</title><style>body{{font-family:system-ui,-apple-system,Segoe UI,Tahoma,sans-serif;max-width:1400px;margin:2rem auto;padding:0 1rem;color:#172033;background:#f7f9fc;line-height:1.7}}h1{{color:#123c69}}.meta{{background:#eaf2fb;padding:1rem;border-radius:10px}}table{{width:100%;border-collapse:collapse;background:#fff;box-shadow:0 2px 12px #00000012}}th,td{{border:1px solid #d9e0ea;padding:.65rem;text-align:right;vertical-align:top}}th{{background:#123c69;color:#fff}}tr:nth-child(even){{background:#f5f8fc}}a{{color:#0969da;overflow-wrap:anywhere}}small{{color:#586579}}@media(max-width:800px){{body{{font-size:14px}}table{{display:block;overflow-x:auto;white-space:nowrap}}}}</style></head><body><h1>دليل الاتحادات العربية</h1><div class="meta"><strong>{len(rows)} اتحادًا</strong> · آخر تحقق: 2026-09-27<br>نقطة الانطلاق: <a href="{source}">خريطة SAFF Portal</a>، مع استكمال التحقق من المواقع الرسمية ومصادر مؤسسية مستقلة.<br><small>الروابط الاجتماعية العامة الخاصة بالملتقى استُبعدت من هذا الجدول، وأُبقيت الحسابات المنسوبة لاتحاد بعينه فقط.</small></div><p><a href="README.md">المنهجية والنسخة Markdown</a> · <a href="data.csv">تنزيل CSV</a></p><table><thead><tr><th>#</th><th>الاتحاد</th><th>الموقع المباشر</th><th>الشبكات الاجتماعية</th><th>RSS/Atom</th></tr></thead><tbody>{''.join(trs)}</tbody></table><h2>المنهجية</h2><p>استُخدمت خريطة SAFF Portal كنقطة انطلاق لا كمصدر حصري، ثم جرى التحقق من المواقع الرسمية عبر صفحاتها ومصادر مؤسسية مستقلة. عدم العثور على خلاصة لا يثبت عدم وجودها خلف مسار آخر.</p><p><a href="{source}">المصدر الأصلي</a> · <a href="https://saffportal.org/">SAFF Portal</a></p></body></html>'''
open('index.html','w',encoding='utf-8').write(page)
print('created',len(rows),'records')
