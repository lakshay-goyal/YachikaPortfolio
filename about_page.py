# import streamlit as st
# # import streamlit_shadcn_ui as ui

# def about_page():
#     # Custom CSS for the About page with enhanced design
#     st.markdown("""
#     <style>
#         /* Advanced styling for About page */
#         .about-header {
#             background: linear-gradient(45deg, #3b82f6, #8b5cf6);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             font-weight: 900;
#             font-size: 3rem;
#             margin-bottom: 2rem;
#             text-align: center;
#         }

#         .professional-journey {
#             background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
#             border-left: 5px solid #8b5cf6;
#             padding: 25px;
#             border-radius: 12px;
#             margin-bottom: 1.5rem;
#             transition: all 0.3s ease;
#         }

#         .professional-journey:hover {
#             transform: translateY(-5px);
#             box-shadow: 0 10px 20px rgba(0,0,0,0.1);
#         }

#         .code-text {
#             background-color: rgba(139, 92, 246, 0.2);
#             padding: 3px 8px;
#             border-radius: 6px;
#             font-family: 'Cascadia Code', monospace;
#             color: #8b5cf6;
#             font-weight: 600;
#         }

#         .metrics-grid {
#             display: grid;
#             grid-template-columns: repeat(3, 1fr);
#             gap: 20px;
#             margin-top: 1.5rem;
#         }

#         .metric-card {
#             background: linear-gradient(145deg, #ffffff, #f0f5ff);
#             border-radius: 15px;
#             padding: 20px;
#             text-align: center;
#             box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #ffffff;
#             transition: all 0.3s ease;
#         }

#         .metric-card:hover {
#             transform: scale(1.05);
#             box-shadow: 12px 12px 24px #d1d9e6, -12px -12px 24px #ffffff;
#         }

#         .metric-value {
#             font-size: 2.5rem;
#             font-weight: 800;
#             background: linear-gradient(90deg, #3b82f6, #8b5cf6);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#         }

#         .metric-label {
#             font-size: 1rem;
#             color: #64748b;
#             margin-top: 10px;
#         }

#         .skill-container {
#             background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
#             border-radius: 12px;
#             padding: 20px;
#             margin-bottom: 1rem;
#         }

#         .skill-progress {
#             display: flex;
#             align-items: center;
#             margin-bottom: 10px;
#         }

#         .skill-name {
#             flex-grow: 1;
#             margin-right: 15px;
#             font-weight: 600;
#             color: #4a5568;
#         }
#     </style>
#     """, unsafe_allow_html=True)

#     # Header with gradient text
#     st.markdown('<h1 class="about-header">About Me</h1>', unsafe_allow_html=True)
    
#     # Main content columns
#     col1, col2 = st.columns([2, 1])
    
#     with col1:
#         # Professional Journey section with enhanced styling
#         st.markdown("""
#         <div class="professional-journey">
#             <h3 style="color: #8b5cf6; margin-bottom: 15px;">Professional Journey</h3>
            
#             <p>I'm a passionate <strong>full-stack developer</strong> dedicated to pushing technological boundaries, with expertise in:</p>
            
#             <ul style="list-style-type: none; padding-left: 0; display: flex; gap: 10px; flex-wrap: wrap;">
#                 <li><span class="code-text">Web Technologies</span></li>
#                 <li><span class="code-text">Cloud Computing</span></li>
#                 <li><span class="code-text">Machine Learning</span></li>
#                 <li><span class="code-text">AI Solutions</span></li>
#             </ul>
            
#             <p>With over 6 years of experience, I craft innovative solutions that bridge cutting-edge technologies with real-world challenges, transforming complex problems into elegant, efficient systems.</p>
#         </div>
#         """, unsafe_allow_html=True)

#     with col2:
#         # Enhanced metrics design with grid layout
#         st.markdown("""
#         <div class="metrics-grid">
#             <div class="metric-card">
#                 <div class="metric-value">6+</div>
#                 <div class="metric-label">Years Experience</div>
#             </div>
#             <div class="metric-card">
#                 <div class="metric-value">50+</div>
#                 <div class="metric-label">Projects</div>
#             </div>
#             <div class="metric-card">
#                 <div class="metric-value">15+</div>
#                 <div class="metric-label">Technologies</div>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

#     # Divider
#     st.markdown("---")  

#     # Skills visualization with custom design
#     st.markdown('<h3 style="color: #8b5cf6; text-align: center; margin-bottom: 20px;">Core Skills</h3>', unsafe_allow_html=True)
    
#     # Skill progress bars with enhanced styling
#     skills = {
#         "Python & Data Science": 90,
#         "Full-Stack Web Development": 85,
#         "Cloud & DevOps": 80,
#         "Machine Learning & AI": 75,
#         "System Architecture": 70
#     }
    
#     st.markdown('<div class="skill-container">', unsafe_allow_html=True)
#     for skill, percentage in skills.items():
#         st.markdown(f"""
#         <div class="skill-progress">
#             <div class="skill-name">{skill}</div>
#             <div style="width: 200px; background-color: #e2e8f0; border-radius: 10px; overflow: hidden;">
#                 <div style="width: {percentage}%; background: linear-gradient(90deg, #3b82f6, #8b5cf6); height: 10px; border-radius: 10px;"></div>
#             </div>
#             <div style="margin-left: 15px; color: #4a5568;">{percentage}%</div>
#         </div>
#         """, unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)



# def main():
#     about_page()

# if __name__ == "__main__":
#     main()


import streamlit as st
import base64

def get_base64_image(image_path):
    """Convert image to base64 for embedding"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def about_page():
    # Enhanced custom CSS with additional improvements
    st.markdown("""
    <style>
        /* Advanced styling for About page */
        .stApp {
            background-color: #f4f6f9;
            font-family: 'Inter', sans-serif;
        }

        .about-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3.5rem;
            margin-bottom: 2.5rem;
            text-align: center;
            letter-spacing: -2px;
            animation: gradient-shift 5s ease infinite;
        }

        @keyframes gradient-shift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .professional-journey {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.08);
            transition: all 0.4s ease;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.18);
        }

        .professional-journey:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.12);
        }

        .code-text {
            background-color: rgba(139, 92, 246, 0.1);
            padding: 5px 10px;
            border-radius: 8px;
            font-family: 'Cascadia Code', monospace;
            color: #8b5cf6;
            font-weight: 600;
            margin: 0 5px;
            display: inline-block;
            transition: background-color 0.3s;
        }

        .code-text:hover {
            background-color: rgba(139, 92, 246, 0.2);
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 2rem;
        }

        .metric-card {
            background: linear-gradient(145deg, #ffffff, #f0f5ff);
            border-radius: 20px;
            padding: 25px;
            text-align: center;
            box-shadow: 10px 10px 20px #d1d9e6, -10px -10px 20px #ffffff;
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }

        .metric-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle at center, rgba(59,130,246,0.1) 0%, transparent 70%);
            transform: rotate(-45deg);
            opacity: 0;
            transition: opacity 0.5s;
        }

        .metric-card:hover::before {
            opacity: 1;
        }

        .metric-card:hover {
            transform: scale(1.05) rotate(2deg);
        }

        .metric-value {
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -2px;
        }

        .skill-progress {
            margin-bottom: 15px;
            background-color: rgba(59,130,246,0.05);
            border-radius: 15px;
            padding: 10px;
            transition: background-color 0.3s;
        }

        .skill-progress:hover {
            background-color: rgba(59,130,246,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    # Header with gradient text and animation
    st.markdown('<h1 class="about-header">About Me</h1>', unsafe_allow_html=True)
    
    # Main content columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Professional Journey section with enhanced styling
        st.markdown("""
        <div class="professional-journey">
            <h3 style="color: #8b5cf6; margin-bottom: 20px; font-size: 1.8rem;">Professional Journey</h3>
            <p style="color: #8b5cf6;">I'm a passionate <strong>full-stack developer</strong> dedicated to pushing technological boundaries, with expertise in:</p>  <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 15px;">
                <span class="code-text">Web Technologies</span>
                <span class="code-text">Cloud Computing</span>
                <span class="code-text">Machine Learning</span>
                <span class="code-text">AI Solutions</span>
            </div>
            <div  style="color: #8b5cf6;">With over 6 years of experience, I craft innovative solutions that bridge cutting-edge technologies with real-world challenges, transforming complex problems into elegant, efficient systems.</div>
            
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Enhanced metrics design with grid layout and hover effects
        st.markdown("""
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-value">6+</div>
                <div style="color: #64748b; margin-top: 10px;">Years Experience</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">50+</div>
                <div style="color: #64748b; margin-top: 10px;">Projects</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">15+</div>
                <div style="color: #64748b; margin-top: 10px;">Technologies</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="About Me",
        page_icon=":rocket:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    about_page()

if __name__ == "__main__":
    main()