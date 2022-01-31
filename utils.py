import PyPDF2
from pathlib import Path
import pandas as pd
import string


class Preprocessing():
    
    def __init__(self):
        self.sentences_to_remove=['©2013 Project Management Institute.', 'A Guide to the Project Management Body of Knowledge (PMBOK','® Guide) Œ Fifth Edition ','11 - PROJECT RISK MANAGEMENT','Probability and Impact MatrixProbability0.90\n0.70\n0.50\n0.30\n0.100.05\n0.04\n0.03\n0.02\n0.010.05/Very Low\n0.09\n0.07\n0.05\n0.03\n0.010.10/Low\n0.18\n0.14\n0.10\n0.06\n0.020.20/Moderate0.36\n0.28\n0.20\n0.12\n0.040.40/High0.72\n0.56\n0.40\n0.24\n0.080.80/Very High\nImpact (numerical scale) on an objective  (e.g., cost, time, scope or quality)\nEach risk is rated on its probability of occurring and impact on an objective if it does occur.', "The organization's \nthresholds for low, moderate or high risks are shown in the matrix and determine whether the risk is scored \nas high, moderate or low for that objective.\nThreats0.05\n0.04\n0.03\n0.02\n0.010.05/Very Low\n0.09\n0.07\n0.05\n0.03\n0.010.10/Low\n0.18\n0.14\n0.10\n0.06\n0.020.20/Moderate0.36\n0.28\n0.20\n0.12\n0.040.40/High0.72\n0.56\n0.40\n0.24\n0.080.80/Very High\nOpportunities\nFigure 11-10", "Licensed To: Jorge Diego Fuentes Sanchez PMI MemberID: 2399412This copy is a PMI Member benefit, not for distribution, sale, or reproduction."]
    
    def create_new_pdf_file(self,path,new_file_path,start_page,end_page):
        pdf_file = open(path, mode='rb')
        pdf_read = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for n in range(start_page, end_page):
            page = pdf_read.getPage(n)
            pdf_writer.addPage(page)
            with Path(new_file_path).open(mode="wb") as output_file:
          
                pdf_writer.write(output_file)
            
    def remove_punctions(self,text):
        # replace the punctuations by ''
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)
        
            
            
    def remove_header(self,new_pdf_read):
        text=[]
        for i in range(0,new_pdf_read.getNumPages()):
            current_page = new_pdf_read.getPage(i)
            current_page_text=current_page.extractText()
            current_page_text=current_page_text.replace(str(i+309),"")
            current_page_text=current_page_text.replace("identi˜cation","identification")
            current_page_text=current_page_text.replace("de˜ning","defining")
            current_page_text=current_page_text.replace("['Š','Œ']"," ")
            current_page_text=current_page_text.replace("identi˜ed","identified")
            current_page_text=current_page_text.replace("project™s","project's") 
            current_page_text=current_page_text.replace("organization™s","organization's") 
            current_page_text=current_page_text.replace("in˚uenced","influenced")
            current_page_text=current_page_text.replace("classi˜ed","classified")
            current_page_text=current_page_text.replace("speci˜c","specific")
            current_page_text=current_page_text.replace("De˜nes","Defines")
            current_page_text=current_page_text.replace("clari˜es","clarifies")
            current_page_text=current_page_text.replace("de˜ned","defined") 
            current_page_text=current_page_text.replace("Stakeholders™","Stakeholders")
            current_page_text=current_page_text.replace("stakeholders™","stakeholders")
            current_page_text=current_page_text.replace("˜les","files")
            current_page_text=current_page_text.replace("re˜ned","refined")
            current_page_text=current_page_text.replace("identi˜es","identifies")
            current_page_text=current_page_text.replace("˜shbone","fishbone") 
            current_page_text=current_page_text.replace("in˚uences","influences")
            current_page_text=current_page_text.replace("experts™","experts")
            current_page_text=current_page_text.replace("bene˜t","benefit")
            current_page_text=current_page_text.replace("risk™s","risk's") 
            current_page_text=current_page_text.replace("˜rst-of-its-kind","first-of-its-kind")
            current_page_text=current_page_text.replace("Speci˜cally","Specifically")
            current_page_text=current_page_text.replace("˜rst","first")
            current_page_text=current_page_text.replace("dif˜cul","difficul")
            current_page_text=current_page_text.replace("˜nal","final")
            current_page_text=current_page_text.replace("in˚uence","influence")
            current_page_text=current_page_text.replace("TechniquesCommonly","Techniques Commonly")
            current_page_text=current_page_text.replace("bene˜ts","benefits")
            current_page_text=current_page_text.replace("˜gure","figure")
            current_page_text=current_page_text.replace("de˜ne","define") 
         
            current_page_text=current_page_text.replace("con˜dence","confidence")
            current_page_text=current_page_text.replace("quanti˜cation","quantification")
            current_page_text=current_page_text.replace("re˚ect","reflect")
            current_page_text=current_page_text.replace("signi˜cance","significance")
            current_page_text=current_page_text.replace("de˜nitions","definitions")
            current_page_text=current_page_text.replace("˜nancial","financial") 
            current_page_text=current_page_text.replace("˜xed-price contract","fixed-price contract")
            current_page_text=current_page_text.replace("signi˜cantly","significantly") 
            current_page_text=current_page_text.replace("de˜nitely","definitely")
            current_page_text=current_page_text.replace("˜nish","finish")
            current_page_text=current_page_text.replace("prede˜ned","predefined")
            current_page_text=current_page_text.replace("suf˜cient","sufficient")
            current_page_text=current_page_text.replace("staf˜ng","staffing")
            current_page_text=current_page_text.replace("modi˜ed","modified")
            current_page_text=current_page_text.replace("Speci˜c","Specific")
            current_page_text=current_page_text.replace("ef˜ciency","efficiency")
            current_page_text=current_page_text.replace("quanti˜able","quantifiable")
            current_page_text=current_page_text.replace("dif˜cult","difficult")
            current_page_text=current_page_text.replace("unidenti˜ed","unidentified")
            current_page_text=current_page_text.replace("RequestsImplementing","Requests Implementing")
            current_page_text=current_page_text.replace("R\necommended preventive actions","Recommended preventive actions")
            current_page_text=current_page_text.replace("UpdatesProject","Updates Project") 
            current_page_text=current_page_text.replace("Assets UpdatesThe risk","Assets Updates The risk")
            current_page_text=current_page_text.replace("˚ow","flow")
            current_page_text=current_page_text.replace("pro˜le","profile")
            current_page_text=current_page_text.replace("Strategies \nSome","Strategies Some")
            for sentence in self.sentences_to_remove: 
                current_page_text=current_page_text.replace(sentence,"")
            text.append(current_page_text)
            
        return text
    
    
    
    ''' 
    Probability and Impact MatrixProbability0.90\n0.70\n0.50\n0.30\n0.100.05\n0.04\n0.03\n0.02\n0.010.05/Very Low\n0.09\n0.07\n0.05\n0.03\n0.010.10/Low\n0.18\n0.14\n0.10\n0.06\n0.020.20/Moderate0.36\n0.28\n0.20\n0.12\n0.040.40/High0.72\n0.56\n0.40\n0.24\n0.080.80/Very High\nImpact (numerical scale) on an objective  (e.g., cost, time, scope or quality)\nEach risk is rated on its probability of occurring and impact on an objective if it does occur. The organization's \nthresholds for low, moderate or high risks are shown in the matrix and determine whether the risk is scored \nas high, moderate or low for that objective.\nThreats0.05\n0.04\n0.03\n0.02\n0.010.05/Very Low\n0.09\n0.07\n0.05\n0.03\n0.010.10/Low\n0.18\n0.14\n0.10\n0.06\n0.020.20/Moderate0.36\n0.28\n0.20\n0.12\n0.040.40/High0.72\n0.56\n0.40\n0.24\n0.080.80/Very High\nOpportunities\nFigure 11-10
    
    def replace_words(self,list_of_text):
        identi˜cation,de˜ning,Š-> espace,identi˜ed,project™s or organization™s,in˚uenced,classi˜ed,speci˜c,,in˚uence,re˚ect,,bene˜t,˚ow->flow,,de˜ne,pro˜le, de˜nitions, ,De˜nes, clari˜es,de˜ned,Stakeholders™,stakeholders™,˜les->files,re˜ned->refined,identi˜es,˜shbone->fishbone, in˚uences, ,experts™, ,risk™s,˜rst-of-its-kind->first of its kind,Speci˜cally, ˜rst,dif˜cult, ˜nal,Techniques Commonly,bene˜ts,˜gure,Œ->espace,-,con˜dence,quanti˜cation,,signi˜cance, ˜nancial,˜xed-price contract,signi˜cantly, de˜nitely,,˜nish,Strategies \nSome,prede˜ned,  suf˜cient, staf˜ng, modi˜ed , Speci˜c, ef˜ciency, ,  quanti˜able, RequestsImplementing, unidenti˜ed, R\necommended preventive actions, UpdatesProject, Assets UpdatesThe risk
            
        
            
        return text
        
        '''
                    
    
    
    
    