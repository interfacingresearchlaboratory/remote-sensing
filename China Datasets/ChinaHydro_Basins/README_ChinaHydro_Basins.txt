README  -  ChinaHydro_Basins

"Hydrographic Basins of China"
Edited by Lex Berman

Draft:  20121009

License:  Creative Commons: Attribution-NonCommercial-Share
http://creativecommons.org/licenses/by-nc-sa/3.0/

Published by:  Skinner Data Archive (Regional Systems Analysis)

Distribution URL:   http://dvn.iq.harvard.edu/dvn/dv/hrs

Citation:  "Hydrographic Basins of China," Compiled by Lawrence Crissman, and edited by Lex Berman.  Skinner Data Archive, 2012.


Source:  
Derived and modified by the G. W. Skinner Regional Systems Analysis Lab from the "China Hydrography" dataset compiled by Lawrence Crissman, (c) ACASIAN 1998.  Produced by the Australian Centre of the Asian Spatial Information and Analysis Network, Griffith University, Australia, under the direction of L. W. Crissman. Copyright to these spatial data is owned by Griffith University.  Revised for distribution by Lex Berman (2012).

Original data sources:   
1) Land-use Map of China [LUMC] General Editor, Wu Chuanjun, Chinese Academy of Sciences. (Beijing:  Science Press,  1990)

Alternatives:   See also the USGS HYDRO1K dataset:  http://webgis.wr.usgs.gov/globalgis/metadata_qr/metadata/hydro1k.htm

Composition:  The ChinaHydro data contains two higher level layers for MajorBasins (40 polygons) and SubBasins (349 polygons), serving as a national level framework for the detailed Province-level basins in the ACASIAN "China Hydrography" dataset (29,484 polygons).

For the MajorBasins layer, Chinese names have been added by the editor based on the Zhongguo Heliu Xitu (China River System Map), to which were added five top level basins for Taiwan, Hainan, Zanda, Kongka Pass, and the Chumbi Valley.   

For the SubBasins layer, Chinese names were partially restored (from the original ArcInfo coverage that ACASIAN provided to the Regional Systems Lab), by importing the attribute table pat.adf as an encoded text file into OpenOffice and retrieving each Chinese name using a string search.   This became necessary because original BIG5 coverage could not be opened in ArcMap 10.  Note, additional names were added by the editor that were not found in the coverage, especially in the Tibetan Plateau.  The additional names were derived from Wikimapia (for romanizations) and ditu.google.cn (for Chinese characters).


Attributes - MajorBasins  (4o features):

MBASIN_ID  =  Unique Identifier for each Major Basin
MNAME =  English name for each Major Basin
CATCHMNT =  destination body of water basin eventually drains into
MNAME_CH  =  Full Chinese character name for each Major Basin
LABEL_CH  =  Short Chinese name for labeling purposes


Attributes - SubBasins (349 features):

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