import re

def fix_main(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    main_match = re.search(r'<main.*?class="(.*?)".*?>', content)
    if not main_match:
        return
    classes = main_match.group(1)
    
    if "bg-charcoal-900" in classes: 
        return  # Already processed

    inner_classes = ["mx-auto", "px-6", "relative", "z-10", "w-full"]
    main_classes = ["flex-grow", "relative", "bg-charcoal-900", "w-full", "overflow-hidden", "border-t", "border-gray-800"]
    
    for cls in classes.split():
        if cls.startswith("max-w-") or cls.startswith("py-") or cls.startswith("text-") or cls.startswith("animate-") or cls.startswith("space-y-"):
            inner_classes.append(cls)

    inner_class_str = " ".join(inner_classes)
    main_class_str = " ".join(main_classes)

    new_main_open = f"""    <main class="{main_class_str}">
        <!-- Abstract Background shapes -->
        <div class="absolute top-0 right-0 w-[800px] h-[800px] bg-harvard-600/10 rounded-full blur-[100px] mix-blend-screen pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-gold-400/5 rounded-full blur-[100px] mix-blend-screen pointer-events-none"></div>
        <div class="absolute top-1/2 left-1/3 w-[600px] h-[600px] bg-harvard-800/10 rounded-full blur-[120px] mix-blend-screen pointer-events-none"></div>
        
        <div class="{inner_class_str}">"""

    content = re.sub(r'<main.*?>', new_main_open, content, count=1)
    content = content.replace('</main>', '        </div>\n    </main>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

fix_main('curriculum.html')
fix_main('privacy.html')
fix_main('terms.html')
