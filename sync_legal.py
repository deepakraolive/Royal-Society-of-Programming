import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract Tailwind config + Style from index.html
head_block_match = re.search(r'(<script>\s*tailwind\.config.*?)</head>', idx_content, re.DOTALL)
head_assets = head_block_match.group(1) if head_block_match else ""

# Extract neural network script
nn_script_match = re.search(r'(<!-- Neural Network Animation Script -->.*?</script>)\s*</body>', idx_content, re.DOTALL)
nn_script = nn_script_match.group(1) if nn_script_match else ""

# 1. Update Curriculum Header
with open('curriculum.html', 'r', encoding='utf-8') as f:
    curr_content = f.read()

curr_content = curr_content.replace(
    '<header class="w-full p-8 flex justify-between items-center bg-[#020202] border-b border-gray-800">',
    '<header class="absolute top-0 left-0 w-full p-8 flex justify-between items-center z-20">'
)
# Ensure padding on the section so it doesn't overlap now that header is absolute
curr_content = curr_content.replace('class="relative hero-bg py-24', 'class="relative hero-bg py-32')

with open('curriculum.html', 'w', encoding='utf-8') as f:
    f.write(curr_content)

# 2. Update Privacy and Terms
def process_legal_page(filename, title1, title2, date_str):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject Head
    content = re.sub(r'<script>\s*tailwind\.config.*?</style>', head_assets, content, flags=re.DOTALL)

    # Add NN script
    if 'Neural Network Animation Script' not in content:
        content = content.replace('</body>', '\n    ' + nn_script + '\n</body>')

    # Replace Header style
    content = content.replace(
        '<header class="w-full p-8 flex justify-between items-center bg-[#020202] border-b border-gray-800">',
        '<header class="absolute top-0 left-0 w-full p-8 flex justify-between items-center z-20">'
    )

    # Form Hero Section
    # Remove the old h1 and date from main
    content = re.sub(r'<h1.*?>.*?</h1>\s*<p class="text-sm.*?>.*?</p>', '', content, flags=re.DOTALL)

    hero_html = f"""<!-- Page Header -->
    <section class="relative hero-bg py-32 border-b border-gray-800 overflow-hidden">
        <canvas id="neural-canvas" class="absolute top-0 left-0 w-full h-full z-0 pointer-events-none opacity-60"></canvas>
        <div class="max-w-5xl mx-auto px-6 relative z-10 text-center animate-fade-in-up">
            <h1 class="text-5xl md:text-7xl font-serif font-bold text-white mb-6">{title1} <span class="gradient-text">{title2}</span></h1>
            <p class="text-sm text-gray-500 uppercase tracking-widest font-bold">Last updated: {date_str}</p>
        </div>
    </section>

    <!-- Main Content -->"""
    
    content = content.replace('<!-- Main Content -->', hero_html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

process_legal_page('privacy.html', 'Privacy', 'Policy', 'March 2026')
process_legal_page('terms.html', 'Terms', '& Conditions', 'March 2026')
