from django.shortcuts import render
from .models import Education, WorkExperience, ProjectExperience, Publication
from datetime import date

def resume_view(request):
    education = [
        {
            'school': '中国水利水电科学研究院',
            'degree': '水文学及水资源',
            'start_date': date(2021, 9, 1),
            'end_date': date(2024, 6, 30)
        },
        {
            'school': '长安大学',
            'degree': '水利水电工程',
            'start_date': date(2016, 9, 1),
            'end_date': date(2020, 6, 30)
        }
    ]
    
    # 工作经历
    work = [
        {
            'company': '陕西思极科技有限公司',
            'position': 'AI应用工程师',
            'description': """1. 研究垂直领域多模态大模型（如电力、水利）及其应用场景的开发（包括Prompt、RAG、Agent等技术），支撑智能决策、知识推理、自动化流程等应用；
                              2. 研究机器学习、深度学习及行业专用模型，推动其在电力与水利场景中实现时序预测与优化配置，提升数据驱动的预测准确性与智能决策能力
            """,
            'start_date': date(2025, 2, 17),
            'end_date': date(2025, 9, 22)
        },
        {
            'company': '南京钛能科技股份有限公司',
            'position': '研发工程师',
            'description': """1. 主导水利知识平台的建设，利用大模型、知识图谱等先进技术，推动水利行业知识库的构建与应用，提升行业智能化水平;
                              2. 负责流域水文预报、水库调度及大坝安全监测算法的研发，结合水利专业模型与机器学习算法，实现中小型水库的洪水预报、调度优化以及大坝的安全监测；
                              3. 根据业务需求，设计并开发模型算法，撰写相关学术论文与专利，推动科研成果的转化与应用。
                            """,
            'start_date': date(2024, 7, 8),
            'end_date': date(2025, 2, 12)
        }
    ]
    
    # 项目经验
    projects = [
        {
            'title': '数字化场景智慧管理助手',
            'description': '构建基于人工智能的场景智能审查模型。',
            'tech_stack': 'Sentence Transformers框架 + Embedding模型 + 相似度算法 + chromadb + Langchain框架 + Prompt Engineering + Structured output',
            'link': 'https://github.com/Tomzhuiowewie/checkReview'
        },
        {
            'title': '基建无计划作业智能问数',
            'description': '构建智能问数模型',
            'tech_stack': 'dify框架 + RAG(库表结构、标准SQl) + LLM(SQL生成) + SQL查询 + LLM(数据分析总结) + python(可视化展示)',
            'link': '#'
        }
    ]
    
    # 论文
    publications = [
        {
            'title': '水利关系型数据库与图数据库集成及应用研究',
            'journal': '中国知网（毕业论文）',
            'year': 2024,
            'link': 'https://kns.cnki.net/kcms2/article/abstract?v=4QAaWarC2DT0omil0SSuuQr9JW13CWP31fUcPFsL-xl_G_SrHg8f-Wov1i2L-52A7t8er1FZ3TJdbonHd6ObGcb5S-VrlqdWeQLKEu1KCzt9U3_HlrkQh6N6PLUf6nRU2N-sJQvaHGIhJBbXnvajrwIueR3DTvyEklfak_YeDVYlr_xLxK8u826XnAHJkDEb&uniplatform=NZKPT&language=CHS'
        },
        {
            'title': '水利多领域知识图谱关联融合方法研究',
            'journal': '人民黄河',
            'year': 2024,
            'link': 'https://kns.cnki.net/kcms2/article/abstract?v=4QAaWarC2DTZSDkFbnly5kWWBX3nAMmbJn7n6bDhmUZeiL5hTjCO-WHPb1p6bYf09s58weEkNlboOA7DNCBEA91fVUbcH30Il3THBZwdyY0KHZInxRUpJxTXQR_sdOCXa9FiX1960TSFQ0EygYLN9Xf2fsKuDnbZ&uniplatform=NZKPT&language=CHS'
        },
    ]
    
    context = {
        'education': education,
        'work': work,
        'projects': projects,
        'publications': publications
    }
    return render(request, 'resume.html', context)
