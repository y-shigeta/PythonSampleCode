import docx
from docx import Document
from docx.shared import Inches
from os import path
import logging

OrgWord = "SampleWord.docx"
NewWord = "./Updated_"+OrgWord

#Initialize logging
LogfileName = "./"+path.splitext(__file__)[0]+".log"
formatter = '%(asctime)s : %(levelname)s : %(message)s'
#logging.basicConfig(level=logging.DEBUG, format=formatter,filename=LogfileName)
logging.basicConfig(level=logging.DEBUG, format=formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#initialize parameters
DefaultFontName = "Meiryo UI"  # or "ＭＳ 明朝" 
DefaultFontSize = "133350"  # This is 10.5pt 
strCurrentHeader = []

# Open Word file
doc = Document(OrgWord)

for parag in doc.paragraphs:
    logger.debug('paragraph %s', parag.text)

    strCurrentStyle = parag.style.name
    ### Find Style
    if strCurrentStyle == "Heading 1" or strCurrentStyle == "Heading 2" or strCurrentStyle == "Heading 3": 
        strCurrentHeader = parag.text
        strFontSize = parag.style.font.size
        strFontName = parag.style.font.name
        logger.info("[Header]%s [FontName]%s [FontSize]%s [Header]%s",strCurrentStyle,strFontName,strFontSize,strCurrentHeader)                
    elif strCurrentStyle != 'None':
        for run in parag.runs:
            strText = run.text
            strFontName = run.font.name
            strFontSize = str(run.font.size)
            if strFontName != DefaultFontName and strFontName != "None":
                logger.warn("[Bad FontName]%s [Paragraph]:%s",strFontName,strText)
            if strFontSize != DefaultFontSize and strFontSize != "None": # this is 10.5 pt
                logger.warn("[Bad FontSize]%s [Paragraph]:%s",strFontSize,strText)
            logger.debug("[FontName]%s [FontSize]%s [Paragraph]:%s",strFontName,strFontSize,strText)

#doc.save(NewWord)
