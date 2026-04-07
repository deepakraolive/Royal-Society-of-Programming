import re

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract Tailwind config + Style from index.html
head_block_match = re.search(r'(<script>\s*tailwind\.config.*?)</head>', idx_content, re.DOTALL)
head_assets = head_block_match.group(1) if head_block_match else ""

# Extract neural network script
nn_script_match = re.search(r'(<!-- Neural Network Animation Script -->.*?</script>)\s*</body>', idx_content, re.DOTALL)
nn_script = nn_script_match.group(1) if nn_script_match else ""

with open('curriculum.html', 'r', encoding='utf-8') as f:
    curr_content = f.read()

# Replace head section
curr_content = re.sub(r'<script>\s*tailwind\.config.*?</style>', head_assets, curr_content, flags=re.DOTALL)

# Add neural network canvas to hero if not already there
if '<canvas id="neural-canvas"' not in curr_content:
    curr_content = curr_content.replace(
        '<section class="relative bg-[#020202] py-24 border-b border-gray-800 overflow-hidden">',
        '<section class="relative hero-bg py-24 border-b border-gray-800 overflow-hidden">\n        <canvas id="neural-canvas" class="absolute top-0 left-0 w-full h-full z-0 pointer-events-none opacity-60"></canvas>'
    )

# Add the script right before </body> if not already there
if 'Neural Network Animation Script' not in curr_content:
    curr_content = curr_content.replace('</body>', '\n    ' + nn_script + '\n</body>')

with open('curriculum.html', 'w', encoding='utf-8') as f:
    f.write(curr_content)
