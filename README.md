# Flint.AI - Social Media Performance Tool  

[![Flint.AI Demo Video](https://img.shields.io/badge/Watch%20Demo-YouTube-red?logo=youtube)](https://youtu.be/qF0_G8Ljiis?si=oMTUeZiG9PE68Aly)  

**Flint.AI** is a cutting-edge social media performance analysis tool designed to help users gain actionable insights from their content. Built using LangFlow and AstraDB, Flint.AI provides a user-friendly interface for querying engagement metrics, analyzing post performance, and generating AI-driven recommendations.

---

## **Features**  
- Analyze engagement metrics for various post types (e.g., Reels, Carousel, Static Images).  
- AI-powered insights with Groq agents using the llama-groq-70b model.  
- Seamless integration of LangFlow workflows with AstraDB for robust data handling.  
- A prototype landing page built with Next.js for showcasing project features.  

---

## **Tech Stack**  
- **LangFlow:** For building workflows and connecting input-output flows.  
- **AstraDB:** A NoSQL database for storing and querying mock social media data.  
- **Groq Agent:** Powered by llama-groq-70b for intelligent data analysis.  
- **Next.js:** For creating a responsive landing page.  
- **ParseData:** For chunking and structuring query results.

---

## **Project Architecture**  

### **1. Data Preparation**  
- A mock database was created in Excel, containing user data, post types, likes, shares, and comments.  
- The database was uploaded in **PDF format** to AstraDB for querying and analysis.  

---

### **2. Workflow in LangFlow**  
**Nodes Used:**  
- **Chat Input:** Accepts user queries like "Which post type has the highest engagement?"  
- **AstraDB Search:** Connects to AstraDB to retrieve relevant data based on user input.  
- **ParseData:** Processes and structures the retrieved data into manageable chunks for analysis.  
- **Groq Agent:** Uses the llama-groq-70b model to analyze the parsed data and generate insights.  
- **Chat Output:** Displays results and recommendations back to the user.  

**Example Queries:**  
- *"What is the average engagement growth rate across all post types?"*  
  - **Response:** 5.2%  
- *"How does carousel engagement compare to reels?"*  
  - **Response:** Carousel engagement is 15% higher.  
- *"Which post type has the most consistent engagement?"*  
  - **Response:** Photos have 20% higher engagement consistency.  

---

### **3. Landing Page**  
- Created using **Next.js** to showcase Flint.AI's features and capabilities.  
- Features include:  
  - Project structure download.  
  - FAQ section for user queries.  
  - Future scope of Flint.AI.  
  - Contact details for feedback and collaboration.  

---

## **How to Run the Project**  

### Prerequisites  
1. LangFlow installed and configured.  
2. AstraDB account with access to upload and query the database.  
3. Groq agent setup with llama-groq-70b model.  
4. Node.js and Next.js for the landing page.  

### Steps  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo-name/flint.git
   cd flint

