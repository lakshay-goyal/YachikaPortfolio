import streamlit as st

def experience_page():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .experience-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        .experience-card {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(139, 92, 246, 0.05));
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .experience-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .role-title {
            color: #8b5cf6;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .company-name {
            color: #4a5568;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .duration {
            color: #64748b;
            font-style: italic;
            margin-bottom: 15px;
        }
        .description {
            color: #4a5568;
            line-height: 1.5;
        }
        .badge {
            display: inline-block;
            background-color: rgba(139, 92, 246, 0.1);
            color: #8b5cf6;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            margin-right: 5px;
            margin-bottom: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="experience-header">Professional Journey</h1>', unsafe_allow_html=True)

    # Experience Data
    experiences = [
        {
            "role": "Senior Software Engineer",
            "company": "TechInnovate Solutions",
            "duration": "2020 - Present",
            "description": "Spearheading cloud-native app development with microservices architecture.",
            "achievements": ["Reduced costs by 40%", "Led team of 5 developers", "Implemented CI/CD pipelines"],
            "technologies": ["Kubernetes", "AWS", "DevOps"]
        },
        {
            "role": "Software Developer",
            "company": "Digital Dynamics Inc.",
            "duration": "2018 - 2020",
            "description": "Developed innovative web apps focusing on full-stack development and optimization.",
            "achievements": ["Improved performance by 65%", "3 major platforms", "Machine learning integrations"],
            "technologies": ["React", "Node.js", "GraphQL"]
        },
        {
            "role": "Junior Software Engineer",
            "company": "Innovative Tech Labs",
            "duration": "2016 - 2018",
            "description": "Gained foundational experience in software development on diverse projects.",
            "achievements": ["'Rising Talent' award", "Open-source contributions", "Productivity tools"],
            "technologies": ["Python", "Django", "Cloud Computing"]
        }
    ]

    # Render Experience Cards in Two Columns
    col1, col2 = st.columns(2, gap="large")

    for idx, exp in enumerate(experiences):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="experience-card">
                <div class="role-title">{exp['role']}</div>
                <div class="company-name">{exp['company']}</div>
                <div class="duration">{exp['duration']}</div>
                <div class="description">{exp['description']}</div>
                <div>
                    <strong>Key Achievements:</strong>
                    {''.join(f'<span class="badge">{ach}</span>' for ach in exp['achievements'])}
                </div>
                <div style="margin-top: 10px;">
                    <strong>Technologies:</strong>
                    {''.join(f'<span class="badge">{tech}</span>' for tech in exp['technologies'])}
                </div>
            </div>
            """, unsafe_allow_html=True)


    # Additional Professional Summary
    st.markdown("---")
    
    # Professional Summary Section
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### Professional Summary
        A passionate and innovative software engineer with over 6 years of experience in developing cutting-edge technology solutions. 
        Proven track record of delivering high-performance, scalable applications across multiple domains including cloud computing, 
        web development, and machine learning.
        """)
    
    with col2:
        # Professional Metrics
        st.markdown("""
        ### Quick Stats
        - 🚀 3+ Companies
        - 💻 15+ Projects
        - 🏆 5+ Major Achievements
        """)