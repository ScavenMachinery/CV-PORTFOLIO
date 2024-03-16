import streamlit as st
from PIL import Image

def main():
    st.sidebar.markdown("# Federico Panopio")
    st.sidebar.image('profilo.png')

    st.sidebar.write('- Indirizzo email: panopiofederico@gmail.com\n'
             '- Profilo LinkedIn: www.linkedin.com/in/federico-panopio-aa6974247\n'
             '- Profilo GitHub: https://github.com/ScavenMachinery')

    section = st.sidebar.radio('', ('About me','Esperienza Lavorativa', 'Progetti', 'Competenze', 'Formazione', 'Tesi'))

    if section == 'About me':
        show_aboutme()
    elif section == 'Esperienza Lavorativa':
        show_experience()
    elif section == 'Progetti':
        show_projects()
    elif section == 'Competenze':
        show_skills()
    elif section == 'Formazione':
        show_education()
    elif section == 'Tesi':
        show_thesis()


def show_aboutme():
    st.title('ABOUT ME')
    st.write('Hi, my name is Federico, I am a technology enthusiast with a strong passion for information and coding. I have a keen interest in exploring the world of data, mastering all available tools and what innovations have to offer, and approach all the data analysis processes, from data cleansing to data visualization and validation in order to help the decision making in my organization to make plans and data driven actions. ')
    st.title('EXPERIENCE AND INTERESTS')
    st.write('Currently, I am delving into the world of data from both strategic and operational perspectives. My enthusiasm drives me to explore all tools and innovations available in the field, BI, report creation, forecasting, and data visualization.')
    st.title('PERSONAL AND PROFESSIONAL GOALS')
    st.write('I am a passion driven person and my goal is to leverage my knowledge and curiosity in the data field to contribute to the success of my team and the organization as a whole. I am motivated by the challenge of tackling complex problems and finding innovative solutions to enhance efficiency and profitability')
    st.title('WORK APPROACH')
    st.write('I am a hands on type of person which makes me very productive by tackling projects in order to come up with tangible solutions and immediatly contribute to the success of my team and the organization as a whole. I am motivated by the challenge of tackling complex problems and finding innovative solutions to enhance efficiency and profitability')
    st.title('CERTIFICATES')
    st.image('Coursera Google Data analyst certificate.png')
    st.image('udemy excel certificate.jpg')

def show_experience():
    st.title('ESPERIENZA LAVORATIVA')
    st.image('logo.bettershop.png')
    st.write('- Nome dell\'azienda: **Bettershop SRL**\n'
             '- Posizione: Data Analyst\n'
             '- Periodo lavorativo: 01/08/2023 - current\n'
             '- Descrizione delle mansioni:\n'
             '    - Market analysis\n'
             '    - Automation workflows\n'
             '    - Reporting\n'
             '    - Dashboards and data visualization\n'
             '    - Forecasting\n'
             '- Nome dell\'azienda: **Bettershop SRL**\n'
             '- Posizione: Internship Junior Accountant\n'
             '- Periodo lavorativo: 01/02/2023 - 01/08/2023\n'
             '- Descrizione delle mansioni:\n'
             '    - Keeping track of Cash flow\n'
             '    - Reporting\n'
             '    - General accounting tasks\n')
    st.write('----------------------------------------------------------------')
    st.image('L&C.jpeg', width=100)
    st.write(
             '- Nome dell\'azienda: **Language & Consulting**\n'
             '- Posizione: Commercial internship\n'
             '- Periodo lavorativo: 01/10/2021 - 01/03/2022\n'
             '- Descrizione delle mansioni: Client and business scounting\n')
    st.write('----------------------------------------------------------------')
    st.write(
             '- Nome dell\'azienda: **Caffetteria Dali**\n'
             '- Posizione: part time Bartender and university student\n'
             '- Periodo lavorativo: 01/10/2018 - 01/10/2021 and 01/03/2022 - 01/02/2023\n'
             '- Descrizione delle mansioni: catering and general food service industry tasks\n')
    

def show_projects():
    st.sidebar.write('## Progetti')
    st.title('PROJECTS')
    st.title('**Power Automate invoice worflow automation**')
    st.write('- Breve descrizione: extracting Purchase orders from amazon reports i develop an automation workflow with Power Automate which makes it possible to automatically generate invoices and fill up all the required data in the document field.\n'
             'This project helped our organization at Bettershop to maximize invoice output while minimizing the time to generate them manually saving us time to work on more strategic and important tasks')
    st.image("power automate screenshot.png")
    st.write('----------------------------------------------------------------')
    st.title('**VBA MACRO powered spreadsheets**\n'
             "- Breve descrizione: i've built a convenient spreadsheet to make prices analysis which automatically calculates estimated FBA FEES for amazon logistics management based on products dimensions. The file main feature has a GOAL SEEK VBA CODE to automatically adjust the market price for each item based on the client own marginality expectation")
    st.write('**the following code is just an example and not the actual script of the project**')
    code = '''Sub AutoGoalSeek()
    Dim LastRow As Long
    Dim i As Long
    
    ' Trova l'ultima riga con dati nella colonna A
    LastRow = Cells(Rows.Count, 1).End(xlUp).Row
    
    ' Disabilita gli avvisi
    Application.DisplayAlerts = False
    
    ' Esegui la funzione Goal Seek per ogni riga nella colonna A
    For i = 1 To LastRow
        ' Imposta il valore di colonna C a 0
        Cells(i, 3).Value = 0
        
        ' Esegui la funzione Goal Seek per la cella corrente
        With Cells(i, 3)
            .GoalSeek Goal:=0, ChangingCell:=Cells(i, 2)
        End With
    Next i
    
    ' Riabilita gli avvisi
    Application.DisplayAlerts = True
End Sub
'''
    st.code(code, language='VBA')
    st.write('----------------------------------------------------------------')
    st.title('**Market Analysis Data visualization**\n')
    st.write('- Breve descrizione: a web app developed with the streamlit front end framework with python data cleaning i managed to build a tool to visualize, aggregate and analyze sales data at all level of view: by products, categories and keywords and at revenues and units sold KPIs. The webapp is also linked with a basic DB using GOOGLE SHEET API in order to store and extract data.')
    st.image('data viz.png')

    st.write('----------------------------------------------------------------')
    st.title("**Python's Panda-driven reporting automation**\n")
    st.write("i've built several python scripts which helped me and my organization streamline the reporting workflow by cleaning and calculating the main data we extract from amazon portals. These workflow enable us to prioritize more important tasks than making these time consuming files by hand.")



def show_skills():
    st.sidebar.write('## Competenze')
    st.title('HARD SKILLS')

    col1, col2, col3, col4, col5 ,col6 ,col7= st.columns(7)

    with col1:
        st.image('Excel-Logo.png', use_column_width=True)
    with col2:
        st.image('python logo.jpg', width=90)
    with col3:
        st.image('Pandas_logo.png', width=150)
    with col4:
        st.write('')
    with col5:
        st.image('vba.png', width=180)
    with col6:
        st.write('')
    with col7:
        st.image('streamlit logo.png', width=200)


    st.write('- Advanced Excel user\n'
             '  - PIVOT TABLES\n'
             '  - Macro recordings\n'
             '  - POWER QUERY\n'
             '  - VLOOKUP, XLOOKUP, INDEX(MATCH())\n'
             '- Basic VBA coding experience\n'
             '- Basic knowledge of Automation workflows pipeline with power automate\n'
             '- Entry level experience in Python data analysis and reporting automation with Pandas library\n'
             "- Data visualization with Python's library such as:\n"
             '    - Matplotlib\n'
             '    - Plotly\n'
             '    - Streamlit front end framework\n'
             '- Language skill Level:\n'
             '  - B2 english\n'
             '  - A2 spanish\n')
    st.title('SOFT SKILLS')
    st.write('- Strong sense of duty\n'
             '- Team Work attitude\n'
             '- Willing to help and contribute\n'
             '- Eager for acquiring knowledge and skills\n'
             '- Fast learner\n'
             '- Proactive\n'
             '- Project based and hands-on approach to learning')
    st.title('OTHER SKILLS')
    st.write('- Basic knowledge of electronic circuitry\n'
             '- Basic skills in soldering, designing and building electric circuits from scratch\n'
             '- Know ho to manage BOM and budgeting for small electronic projects\n'
             '- Basic arduino coding\n'
             '- Coding in PURE DATA and TYDAL CYCLES (programming language for generative music production)\n')

def show_education():
    st.sidebar.write('## Formazione')
    cola, colb = st.columns([1,2])
    colc, cold = st.columns([1,2])
    cole, colf = st.columns([1,2])
    with cola:
        st.image('unibs.jpg', width= 160)
    with colb:
        st.title('**Titolo di studio universitario:**\n')
        st.write('- Laurea in Economia e Gestione Aziendale indirizzo Business\n'
             '- Università degli studi di Brescia\n')
        
    with colc:
        st.image('lunardi.jpg', width= 160)
    with cold:
        st.title('**Diploma di istruzione tecnica:**\n')
        st.write('- Perito aziendale corrispondente lingue estere\n'
                 '- ITC Istituto Tecnico commerciale Astolfo Lunardi\n')
    with cole:
        st.image('arcades del cid.jpg', width= 160)
    with colf:    
        st.title('**Stage linguistico**')
        st.write('- curso de español nivel avanzado, calificación de APTO\n'
                 '- Arcades del Cid: Escuela de Español para Extranjeros')
    
def show_thesis():
    #st.sidebar.write('## Tesi')
    st.title('**CORPORATE STRATEGIES AGAINST SUPPLY CHAIN DISRUPTIONS: THE SEMICONDUCTOR INDUSTRY CASE**')
    st.write("The core research of the thesis was made by consulting academic papers focused on technologically driven industries, markets data, news articles, industry, and company annual reports By implementing concepts and definitions at a strategy level it was possible to explore the semiconductors industry, with a qualitative and statistical analysis and consequentially their economic interpretations By defining the industry critical points and the external triggers that jeopardize the resiliency of the supply chain and acknowledging the strategic impact of decisions at all levels of strategy, it has been possible to evaluate the different solutions to avoid or minimize the effects of supply chain disruptions")
    st.image('tesi1.png')
    st.image('tesi2.png')
    st.image('tesi3.png')
    st.image('tesi4.png')
    st.image('tesi5.png')
    st.image('tesi6.png')
    st.image('tesi7.png')
    st.image('tesi8.png')
    st.image('tesi9.png')

if __name__ == "__main__":
    main()
