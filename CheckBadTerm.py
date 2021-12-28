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
logging.basicConfig(level=logging.DEBUG, format=formatter,filename=LogfileName)
#logging.basicConfig(level=logging.DEBUG, format=formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#initialize parameters
SearchStrings = ["test", "this", "letter"]
BadChars = ['０', '１', '２', '３', '４', '５', '６', '７', '８', '９','Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ','ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 'ｗ', 'ｘ', 'ｙ', 'ｚ','＼','(',')']
#[chr(0xFF01+i) for i in range(94)]
strCurrentHeader = []


# Open Word file
doc = Document(OrgWord)

for parag in doc.paragraphs:
    logger.debug('paragraph %s', parag.text)

    strCurrentStyle = parag.style.name
    ### Find Style
    if strCurrentStyle == "Heading 1" or strCurrentStyle == "Heading 2" or strCurrentStyle == "Heading 3": 
        strCurrentHeader = parag.text
#        strFontSize = parag.style.font.size
#        strFontName = parag.style.font.name
#       logger.info("[Header]%s [FontName]%s [FontSize]%s [Header]%s",strCurrentStyle,strFontName,strFontSize,strCurrentHeader)                
        logger.info("[Header]%s [Header]%s",strCurrentStyle,strCurrentHeader)

    ### Find Zenkaku and Bad charactors
    strResult = ""
    for BadChar in BadChars:
            logger.debug('BadChar %c', BadChar)
            if parag.text.find(BadChar) > -1:
                    strResult += BadChar

    # Logging Found bad charactors
    if strResult != "":
            logger.debug('strResult %s', strResult)
            logger.warn("[FOUND: Bad Char]%s [Paragraph]%s",strResult,parag.text)

    # Find Strings to check and logging
    for SearchString in SearchStrings:
        logger.debug('SearchString %s', SearchString)
        if parag.text.find(SearchString) > -1:
            logger.warn("[FOUND: Strings To Check]%s [Paragraph]%s",SearchString,parag.text)

#doc.save(NewWord)
