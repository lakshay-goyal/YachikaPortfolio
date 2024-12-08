# import streamlit as st

# def skill_page():
#     st.header("💻 Technical Skills")
    
#     # Define skills with additional metadata
#     skills = {
#         "Programming Languages": [
#             {"name": "Python", "level": 90, "icon": "🐍"},
#             {"name": "JavaScript", "level": 85, "icon": "🟨"},
#             {"name": "TypeScript", "level": 80, "icon": "🔷"}
#         ],
#         "Frameworks": [
#             {"name": "React", "level": 88, "icon": "⚛️"},
#             {"name": "Django", "level": 82, "icon": "🌐"},
#             {"name": "Node.js", "level": 80, "icon": "🟢"}
#         ],
#         "Cloud & DevOps": [
#             {"name": "AWS", "level": 85, "icon": "☁️"},
#             {"name": "Docker", "level": 80, "icon": "🐳"},
#             {"name": "Kubernetes", "level": 75, "icon": "🚢"}
#         ]
#     }
    
#     # Custom styling
#     st.markdown("""
#     <style>
#     .skill-container {
#         background-color: #f0f2f6;
#         border-radius: 10px;
#         padding: 15px;
#         text-align: center;
#         transition: transform 0.3s ease;
#     }
#     .skill-container:hover {
#         transform: scale(1.05);
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#     }
#     .stProgress > div > div {
#         background-color: #4CAF50 !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)
    
#     # Iterate through skill categories
#     for category, skill_list in skills.items():
#         st.subheader(category)
        
#         # Create columns for skills
#         cols = st.columns(len(skill_list))
        
#         # Display skills in containers
#         for i, skill_info in enumerate(skill_list):
#             with cols[i]:
#                 with st.container():
#                     st.markdown(f"""
#                     <div class='skill-container'>
#                         <h3>{skill_info['icon']} {skill_info['name']}</h3>
#                         <div style='margin-top: 10px;'>
#                             <div style='margin-bottom: 5px;'>
#                                 {skill_info['level']}% Proficiency
#                             </div>
#                             <div style='width: 100%;'>
#                                 <div style='width: {skill_info['level']}%; height: 10px; background-color: #4CAF50; border-radius: 5px;'></div>
#                             </div>
#                         </div>
#                     </div>
#                     """, unsafe_allow_html=True)

import streamlit as st
def skill_page():
    st.header("💻 Technical Skills")
    
    # Define skills with additional metadata
    skills = {
        "Programming Languages": [
            {"name": "Python", "level": 90, "icon": "🐍"},
            {"name": "JavaScript", "level": 85, "icon": "🟨"},
            {"name": "TypeScript", "level": 80, "icon": "🔷"}
        ],
        "Frameworks": [
            {"name": "React", "level": 88, "icon": "⚛️"},
            {"name": "Django", "level": 82, "icon": "🌐"},
            {"name": "Node.js", "level": 80, "icon": "🟢"}
        ],
        "Cloud & DevOps": [
            {"name": "AWS", "level": 85, "icon": "☁️"},
            {"name": "Docker", "level": 80, "icon": "🐳"},
            {"name": "Kubernetes", "level": 75, "icon": "🚢"}
        ]
    }
    
    # Custom styling with dark theme
    st.markdown("""
    <style>
    .stApp {
        background-color: #1a1b1e;
        color: #e5e5e5;
    }
    .skill-container {
        background-color: #2b2d31;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .skill-container:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stProgress > div > div {
        background-color: #4CAF50 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Iterate through skill categories
    for category, skill_list in skills.items():
        st.subheader(category)
        
        # Create columns for skills
        cols = st.columns(len(skill_list))
        
        # Display skills in containers
        for i, skill_info in enumerate(skill_list):
            with cols[i]:
                with st.container():
                    st.markdown(f"""
                    <div class='skill-container'>
                        <h3>{skill_info['icon']} {skill_info['name']}</h3>
                        <div style='margin-top: 10px;'>
                            <div style='margin-bottom: 5px;'>
                                {skill_info['level']}% Proficiency
                            </div>
                            <div style='width: 100%;'>
                                <div style='width: {skill_info['level']}%; height: 10px; background-color: #4CAF50; border-radius: 5px;'></div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
