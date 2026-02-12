import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

# --- CONFIGURATION ---
st.set_page_config(page_title="RIDERS TREND ERP Report", layout="wide", page_icon="📊")

# --- DATA CONSTANTS ---
COMPANY = "RIDERS TREND"
AUTHOR = "ZUBAIR BAIG"
DATE = "09.02.2026"

# --- PDF GENERATION CLASS ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'ERP Evaluation Report: {COMPANY}', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, body)
        self.ln()

def create_downloadable_pdf():
    pdf = PDF()
    pdf.add_page()
    
    # 1. Executive Summary
    pdf.chapter_title("1. Executive Summary")
    pdf.chapter_body(f"Prepared By: {AUTHOR}\nDate: {DATE}\n\nThis report evaluates the VB.NET-based ERP system implemented at {COMPANY} (Gloves Manufacturing). The system integrates inventory, finance, sales, purchasing, production, and HR. While operational efficiency has improved, shortfalls exist in automation and real-time reporting.")
    
    # 2. Shortfalls
    pdf.chapter_title("2. Critical Shortfall Report")
    pdf.set_font("Arial", "B", 10)
    pdf.cell(40, 10, "Module", 1)
    pdf.cell(90, 10, "Shortfall", 1)
    pdf.cell(30, 10, "Priority", 1, 1)
    pdf.set_font("Arial", "", 10)
    
    # Shortfall Data
    rows = [
        ("Costing", "Manual overhead allocation", "High"),
        ("MRP", "Manual adjustments required", "High"),
        ("BOM", "No version control", "High"),
        ("Inventory", "Delayed stock valuation", "High"),
        ("HR", "Tax & statutory compliance gaps", "High"),
    ]
    for row in rows:
        pdf.cell(40, 10, row[0], 1)
        pdf.cell(90, 10, row[1], 1)
        pdf.cell(30, 10, row[2], 1, 1)
    
    pdf.ln(10)
    
    # 3. Wages Formula
    pdf.chapter_title("3. Production & Wages Formula")
    pdf.chapter_body("Total Wages = (Basic Time Rate x Hours Worked) + (Piece Rate x Units Produced) + Incentives - Deductions")

    # 4. Recommendations
    pdf.chapter_title("4. Recommendations")
    pdf.chapter_body("- Short Term: Automate cost updates and enable real-time stock valuation.\n- Medium Term: Implement full MRP automation and BOM version control.\n- Long Term: Introduce AI-based material & cost forecasting.")

    return pdf.output(dest='S').encode('latin-1')

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2889/2889315.png", width=100)
st.sidebar.title("📑 Report Navigation")
st.sidebar.markdown(f"**{COMPANY}**")
st.sidebar.markdown(f"*{AUTHOR} | {DATE}*")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Select Section:",
    ["Executive Summary", 
     "Technical Evaluation", 
     "Functional Modules", 
     "Shortfall & Risks", 
     "Production & Wages", 
     "Strategic Recommendations",
     "📥 Download PDF"]
)

# --- PAGE: EXECUTIVE SUMMARY ---
if menu == "Executive Summary":
    st.title("📋 Executive Summary")
    st.info("ERP SUPPORTS BUSINESS OPERATION: FUNCTIONAL FIT")
    
    st.write("""
    This report evaluates the performance, functionality, and business impact of the VB.NET-based ERP system implemented at **RIDERS TREND Gloves Manufacturing**.
    
    The ERP integrates major business operations including:
    * **Finance & Accounting:** Fully covered.
    * **Inventory & Stocks:** Working properly.
    * **Export & Sales:** Working according to requirements.
    * **Imports:** Fully active.
    * **Production:** Running smoothly with fool-proof wages.
    * **HR & Payroll:** Comprehensive reports based on machine attendance.
    """)
    
    st.subheader("System Architecture")
    c1, c2, c3 = st.columns(3)
    c1.metric("Platform", "VB.NET", "Windows Forms")
    c2.metric("Database", "SQL Server", "Microsoft")
    c3.metric("Architecture", "2-Tier", "Client-Server")

# --- PAGE: TECHNICAL EVALUATION ---
elif menu == "Technical Evaluation":
    st.title("⚙️ Technical & Performance Evaluation")
    
    st.subheader("Performance & Reliability")
    st.markdown("""
    1.  **Optimize database queries** and indexes.
    2.  **Use high-performance servers.**
    3.  **Regularly update ERP software** for bug fixes.
    4.  **Implement healthy backup** and disaster recovery strategies.
    """)

    st.subheader("Database Evaluation (SQL Server)")
    st.warning("Issues Identified:")
    st.write("- Data redundancy in some tables.")
    st.write("- Missing indexes leading to slow reports.")
    st.write("- Backup process is sometimes manual.")
    
    st.success("Recommendation: Implement automated backups and optimize indexing.")

# --- PAGE: FUNCTIONAL MODULES ---
elif menu == "Functional Modules":
    st.title("🔍 Functional Module Observations")
    
    tabs = st.tabs(["Finance", "Inventory", "Sales", "Purchase", "Import"])
    
    with tabs[0]:
        st.subheader("Accounting & Finance")
        st.write("The module is central to the ERP system, integrating Sales, Purchase, and HR.")
        st.markdown("""
        * **General Ledger:** Auto-posts journal entries.
        * **Accounts Payable/Receivable:** Tracks vendor invoices and customer aging.
        * **Taxation:** Handles GST/VAT compliance.
        """)
        st.info("Observation: Strong for transaction processing, but reporting flexibility requires customization.")

    with tabs[1]:
        st.subheader("Inventory & Stocks")
        st.markdown("""
        * **Real-time updates:** Stocks updated via GRN.
        * **BOM Integration:** Materials issued according to BOM quantity.
        * **Gap:** Reorder alerts are weak.
        """)

    with tabs[2]:
        st.subheader("Sales & Export")
        st.write("Manages customer database, order processing, and commercial invoicing.")
        st.markdown("""
        * **Automated Billing:** Generates invoices from confirmed sales orders.
        * **Debtor Tracking:** Real-time visibility of outstanding aging.
        * **Gap:** Lack of predictive analytics for payment delays.
        """)
        
    with tabs[3]:
        st.subheader("Purchase Module")
        st.write("Manages procurement, requisitions, and vendor ratings.")
        st.markdown("""
        * **Workflow:** Requisition -> Vendor Selection -> PO -> GRN -> Invoice.
        * **Gap:** Quotation comparison is partially manual.
        """)

    with tabs[4]:
        st.subheader("Import Module")
        st.write("Tracks imported goods and consumption based on approved formulas.")
        st.markdown("""
        * **Stock Update:** Automatic update upon goods receipt.
        * **Compliance:** Tracks customs duties and import documentation.
        """)

# --- PAGE: SHORTFALLS ---
elif menu == "Shortfall & Risks":
    st.title("⚠️ Critical Shortfall Report")
    
    # Create Dataframe for the Table
    data = {
        "Module": ["Costing", "Costing", "MRP", "BOM", "Inventory", "HR & Payroll", "Management"],
        "Shortfall": [
            "Manual overhead allocation", 
            "Delayed cost updates", 
            "Manual adjustments required", 
            "No version control", 
            "Stock valuation delayed", 
            "Tax & statutory compliance gaps",
            "Weak forecasting"
        ],
        "Impact": [
            "Incorrect costing", 
            "Outdated financial info", 
            "Risk of stock-outs", 
            "Production errors", 
            "Financial misreporting", 
            "Compliance risk",
            "Reactive planning"
        ],
        "Priority": ["High", "High", "High", "High", "High", "High", "High"]
    }
    df = pd.DataFrame(data)
    
    # Display Table with Highlighting
    st.dataframe(df.style.applymap(lambda x: 'background-color: #ffcccc' if x == 'High' else '', subset=['Priority']), use_container_width=True)

    st.subheader("Risk Impact Assessment")
    st.markdown("""
    * **Costing Errors:** Leads to financial loss.
    * **Inventory Inaccuracies:** Causes production delays.
    * **Forecasting Gaps:** Results in strategic inefficiency.
    """)

# --- PAGE: PRODUCTION & WAGES ---
elif menu == "Production & Wages":
    st.title("🏭 Production & Wages")
    
    st.subheader("Production Scope")
    st.write("Manages planning, scheduling, BOM, MRP, and Quality Control.")
    
    st.subheader("💰 Wages Calculation Formula")
    st.markdown("The system calculates wages for production staff using the following parameters:")
    
    # Latex Formula
    st.latex(r'''
    Total Wages = (Basic Time Rate \times Hours Worked) + (Piece Rate \times Units Produced) + Incentives - Deductions
    ''')
    
    st.write("**Parameters:**")
    st.write("- **Employee Type:** Skilled, Semi-skilled, Unskilled.")
    st.write("- **Attendance:** Biometric integration.")
    st.write("- **Deductions:** Absenteeism, late coming.")

# --- PAGE: RECOMMENDATIONS ---
elif menu == "Strategic Recommendations":
    st.title("🚀 Strategic Recommendations")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Short-Term")
        st.success("Immediate")
        st.write("- Automate cost updates.")
        st.write("- Enable real-time stock valuation.")
        st.write("- Add budget alerts.")
        
    with col2:
        st.subheader("Medium-Term")
        st.warning("6 Months")
        st.write("- Implement full MRP automation.")
        st.write("- Add BOM version control.")
        st.write("- Enhance HR legal reporting.")
        
    with col3:
        st.subheader("Long-Term")
        st.info("1 Year+")
        st.write("- AI-based material forecasting.")
        st.write("- Predictive KPI dashboards.")
        
    st.subheader("AI-Based Forecasting")
    st.write("Using AI to analyze historical purchase and production data to predict future material needs, reducing wastage and improving profitability.")

# --- PAGE: DOWNLOAD PDF ---
elif menu == "📥 Download PDF":
    st.title("📥 Export Full Report")
    st.write("Click the button below to generate the official PDF report for **RIDERS TREND**.")
    
    if st.button("Generate PDF Document"):
        pdf_data = create_downloadable_pdf()
        st.download_button(
            label="📄 Download ERP_Evaluation_Report.pdf",
            data=pdf_data,
            file_name="ERP_Evaluation_Riders_Trend.pdf",
            mime="application/pdf"
        )