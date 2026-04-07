import re

syllabus = [
  {
    "week": 1,
    "title": "Introduction of AI and Fundamentals Of Python",
    "description": "Content Delivery Duration: 10 Hours",
    "days": [
      {"day": "Day 1", "content": "Introduction to Artificial Intelligence and Machine Learning Applications across domains (business, healthcare, automation, vision, language), Overview of the ML pipeline, types of AI (narrow, general), Key AI problems and techniques, Modern AI Toolkits (TensorFlow, PyTorch)"},
      {"day": "Day 2", "content": "Python basics: Variables, data types, operators, Control flow in Python, Conditional statements, Loops, Variables, data types, operators and practice implementation."},
      {"day": "Day 3", "content": "Python data structures: Lists, tuples, sets, dictionaries"},
      {"day": "Day 4", "content": "Functions, Modules and packages, File handling"},
      {"day": "Day 5", "content": "Introduction to NumPy, Arrays and operations, Mathematical operations with NumPy"}
    ]
  },
  {
    "week": 2,
    "title": "Python for Data Science",
    "description": "Content Delivery Duration: 10 Hours",
    "days": [
      {"day": "Day 6", "content": "Introduction to Pandas, DataFrames and Series, Practical implementation"},
      {"day": "Day 7", "content": "EDA: Data visualization using Matplotlib & Seaborn"},
      {"day": "Day 8", "content": "Types of data, Data pre-processing, data leakage concept, handling missing values, outliers handling, handling categorical data, scaling and normalization, class imbalance handling"},
      {"day": "Day 9", "content": "Feature Engineering: variance threshold Feature Selection, correlation-based removal Feature Selection, forward selection, backward elimination, tree-based feature importance"},
      {"day": "Day 10", "content": "Feature Extraction, creating new features, aggregation features, Dimensionality Reduction: Curse of dimensionality, Principal Component Analysis, explained variance ration, Linear Discriminant Analysis"}
    ]
  },
  {
    "week": 3,
    "title": "Machine Learning Algorithms",
    "description": "Content Delivery Duration: 10 Hours",
    "days": [
      {"day": "Day 11", "content": "Introduction to Machine Learning algorithms, Linear Regression with practical implementation"},
      {"day": "Day 12", "content": "Logistic Regression: Classification problems (Maths behind Logistic algorithm and practical implementation)"},
      {"day": "Day 13", "content": "Types of Linear Regression and Regularization, Different types of Gradient Decent"},
      {"day": "Day 14", "content": "K-Nearest Neighbors (KNN), Decision Tree Algorithm and Random Forest"},
      {"day": "Day 15", "content": "Continuous Assessment (CA) 1"}
    ]
  },
  {
    "week": 4,
    "title": "Evaluation Matrix and Ensemble Learning",
    "description": "Content Delivery Duration: 10 Hours",
    "days": [
      {"day": "Day 16", "content": "Support Vector Machine and Model evaluation: Confusion Matrix, Accuracy, Precision, Recall, F1 Score, ROC Curve, Precision-Recall Curve, Cross Validation"},
      {"day": "Day 17", "content": "Ensemble Learning: Introduction to ensemble learning, Bagging & Boosting Ensembles"},
      {"day": "Day 18", "content": "Cross Validation and Hyperparameter tuning"},
      {"day": "Day 19", "content": "Project-1"},
      {"day": "Day 20", "content": "Project-2"}
    ]
  },
  {
    "week": 5,
    "title": "Unsupervised Learning",
    "description": "Content Delivery Duration: 10 Hours",
    "days": [
      {"day": "Day 21", "content": "Unsupervised Learning: Role of unsupervised learning, Differences between supervised and unsupervised learning, Euclidean, Manhattan, Cosine distances, Choosing appropriate distance metrics"},
      {"day": "Day 22", "content": "K-Means Clustering, Elbow method, K-Medoids, Hierarchical Clustering"},
      {"day": "Day 23", "content": "Introduction to Deep Learning, Neural Networks, Neurons and layers"},
      {"day": "Day 24", "content": "Activation functions, ReLU, Sigmoid, Tanh, Loss functions and optimizers, Gradient Descent, SGD, Adam"},
      {"day": "Day 25", "content": "ANN and Practical Implementation with different Deep learning tools"}
    ]
  },
  {
    "week": 6,
    "title": "CNN and RNN",
    "description": "Content Delivery Duration: 10 Hours",
    "days": [
      {"day": "Day 26", "content": "CNN: Filters (kernels), Stride and padding, Activation functions (ReLU), Pooling layers (Max Pooling, Average Pooling), Flatten layer"},
      {"day": "Day 27", "content": "RNN: types, Sequential data and time-series data, Long Short-Term Memory (LSTM), Gated Recurrent Units (GRU)"},
      {"day": "Day 28", "content": "Project-3"},
      {"day": "Day 29", "content": "Continuous Assessment (CA) 2"},
      {"day": "Day 30", "content": "Project-4"}
    ]
  }
]

# Generate index.html grid code
index_grid = '<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">\n'
for mod in syllabus:
    w = mod['week']
    wstr = f"0{w}"
    title = mod['title']
    desc = mod['description']
    
    index_grid += f"""
                <div class="curr-card glass-dark p-8 rounded-2xl border border-gray-800 group relative flex flex-col h-full overflow-hidden">
                    <div class="absolute top-0 right-0 p-6 text-7xl font-serif text-gray-800/30 group-hover:text-harvard-600/20 transition-colors pointer-events-none select-none">{wstr}</div>
                    <div class="relative z-10 flex flex-col h-full">
                        <h4 class="text-xl font-bold text-white mb-3 group-hover:text-gold-400 transition-colors pr-10"><span class="text-gold-400 font-serif mr-1">Week {w}:</span> {title}</h4>
                        <p class="text-gray-400 leading-relaxed font-light mb-5">{desc}</p>
                        <ul class="mt-auto space-y-3 border-t border-gray-800/60 pt-5">
"""
    for day in mod['days']:
        d_raw = day['day']
        d_num = d_raw.split()[1] if ' ' in d_raw else d_raw
        cont = day['content']
        is_highlight = "Project" in d_raw or "CA" in d_raw or "Project" in cont or "Continuous Assessment" in cont
        text_color = "text-gold-400 font-bold" if is_highlight else "text-gray-400"
        
        index_grid += f"""                            <li class="flex items-start gap-3">
                                <span class="bg-harvard-600/20 text-harvard-500 text-[10px] uppercase font-bold py-1 px-2 rounded-sm mt-0.5 whitespace-nowrap">Day {d_num}</span>
                                <span class="{text_color} text-sm leading-snug">{cont}</span>
                            </li>\n"""
    index_grid += """                        </ul>
                    </div>
                </div>\n"""
index_grid += "            </div>"

# Generate curriculum.html code
curr_content_html = '<div class="space-y-16">\n'
for mod in syllabus:
    w = mod['week']
    wstr = f"0{w}"
    title = mod['title']
    desc = mod['description']
    
    curr_content_html += f"""
            <div class="flex flex-col md:flex-row gap-8 bg-[#111111] p-10 rounded-2xl border border-gray-800 shadow-2xl relative overflow-hidden group hover:border-harvard-600 transition-colors">
                <div class="absolute -top-10 -right-10 text-[180px] font-serif text-[#161616] pointer-events-none group-hover:text-harvard-600/5 transition-colors select-none">{w}</div>
                <div class="md:w-1/3 relative z-10">
                    <h2 class="text-gold-400 font-bold uppercase tracking-widest text-sm mb-2">Module {wstr} / Week {w}</h2>
                    <h3 class="text-3xl font-serif font-bold text-white leading-tight">{title}</h3>
                    <p class="text-gray-500 mt-4 leading-relaxed font-light">{desc}. Master advanced data structures and algorithms in applied environments.</p>
                </div>
                <div class="md:w-2/3 relative z-10 relative pl-0 md:pl-10 md:border-l border-gray-800">
                    <ul class="space-y-6">
"""
    for day in mod['days']:
        d_raw = day['day']
        cont = day['content']
        parts = cont.split(":", 1)
        if len(parts) == 2:
            h = parts[0].strip()
            b = parts[1].strip()
        else:
            h = "Core Concepts"
            b = cont
            
        if "Project" in d_raw or "CA" in d_raw or "Continuous" in cont or "Project" in cont:
            h = "Evaluation Milestone"
            b = cont

        curr_content_html += f"""                        <li><span class="block text-harvard-500 font-bold text-xs uppercase tracking-wider mb-1">{d_raw}: {h}</span><span class="text-gray-300">{b}</span></li>\n"""
        
    curr_content_html += """                    </ul>
                </div>
            </div>\n"""

curr_content_html += """
            <!-- Final CTA -->
            <div class="text-center mt-20 p-12 bg-harvard-800 bg-opacity-30 border border-harvard-600/30 rounded-2xl relative overflow-hidden group">
                <div class="absolute inset-0 bg-gradient-to-br from-harvard-600/10 to-transparent pointer-events-none group-hover:opacity-100 opacity-50 transition-opacity"></div>
                <h3 class="text-3xl font-serif font-bold text-white mb-6 relative z-10">Start Your Elite Learning Journey</h3>
                <p class="text-gray-300 mb-8 max-w-xl mx-auto relative z-10">Ready to transform your technical abilities and master exactly what the industry demands? Registration takes less than three minutes.</p>
                <a href="#" class="relative z-10 inline-flex items-center justify-center bg-gold-500 text-white px-10 py-5 text-sm font-bold uppercase tracking-[0.15em] overflow-hidden rounded shadow-[0_10px_20px_rgba(198,161,91,0.2)] hover:shadow-[0_15px_30px_rgba(198,161,91,0.4)] transition-all">
                    Register Now
                </a>
            </div>
        </div>"""

import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = idx.replace("5-Week Bootcamp", "6-Week Bootcamp")
idx = re.sub(r'<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-20">.*?</div>\s*<!-- Bottom Highlight Bar', index_grid + '\n\n            <!-- Bottom Highlight Bar', idx, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)


# Update curriculum.html
with open('curriculum.html', 'r', encoding='utf-8') as f:
    cur = f.read()

cur = cur.replace("5-Week Bootcamp", "6-Week Bootcamp")
cur = re.sub(r'<div class="space-y-16">.*?</div>\s*</div>\s*</main>', curr_content_html + '\n        </div>\n    </main>', cur, flags=re.DOTALL)

with open('curriculum.html', 'w', encoding='utf-8') as f:
    f.write(cur)
