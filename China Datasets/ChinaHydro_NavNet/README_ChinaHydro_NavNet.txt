README  -  ChinaHydro_NavNet

Navigable Waterways of China, Regional Systems Analysis, G. W. Skinner

Draft:  20121004

License:  Creative Commons: Attribution-NonCommercial-Share
http://creativecommons.org/licenses/by-nc-sa/3.0/

Published by:  Skinner Data Archive (Regional Systems Analysis)

Distribution URL:   http://dvn.iq.harvard.edu/dvn/dv/hrs

Citation:  "ChinaHydro_NavNet" Compiled by Lawrence Crissman, and edited by Lex Berman.  Skinner Data Archive, 2012.

Source:  
Derived from the "Navigable Waterways of China," compiled by Lawrence Crissman, (c) ACASIAN 1998.  Produced by the Australian Centre of the Asian Spatial Information and Analysis Network, Griffith University, Australia, under the direction of L. W. Crissman. Copyright to these spatial data is owned by Griffith University.

Original data sources:   
1) Transport Map of China [TMC] 1:2.5mil(Zhongguo Renmin Gongheguo Jiaotongtu, Beijing:  Jindun Chubanshe, 1990)
2) Communications Map of China [JTT] 1:6mil (Zhongguo Renmin Gongheguo Jiaotongtu, Beijing, Cehui Chubanshe, 1994)
3) Atlas of China [AOC] (English Edition, Beijing, Cartographic Publishing House, 1996).  

Composition:  ChinaHydro_NavNet contains arcs representing sections of rivers in China that are navigable.   This data was revised by the Regional Systems Analysis lab, and edited by Lex Berman.  The river sections are NOT named.  The names are merely joined from the accompanying ChinaHydro_Basins dataset for context.

CHARSET encoding: GBK

Attributes:

NAVNET_ID =  unique ID for river section (arc) that is navigable

TCODE (Original data source for each navigable river section)
   4 = River, navigable by steamships (per Atlas of China)
   30 = River, navigable by other (per JTT, Jiaotongtu)
   50 =  transport canal
   200 = River, navigable by other (per TMC, Transportation Map of China)
   230 = River, navigable by other (per JTT+TMC)

TILE = Soviet Topographic Map Series 1:200 Tile Number Prefix
SBASIN_ID  =  Unique Identifier for each SubBasin
SBASIN_PY =   Pinyin name for each SubBasin
SBASIN_ALT =   Alternate romanized name for each SubBasin
BCODE_GB  =  Guobiao code for each basin
MBASIN_ID  =  Unique Identifier for each Major Basin
MNAME =  English name for each Major Basin
CATCHMNT =  destination body of water basin eventually drains into
MNAME_CH  =  Full Chinese character name for each Major Basin
LABEL_CH  =  Short Chinese name for labeling purposes


Complementary Datasets:  

1)  CHGIS V5 1820 Coded Rivers   http://goo.gl/mAaHp

2)  ChinaMap River Basins   http://goo.gl/JWx11

3)  ChinaMap  Watersheds   http://goo.gl/QDv77 