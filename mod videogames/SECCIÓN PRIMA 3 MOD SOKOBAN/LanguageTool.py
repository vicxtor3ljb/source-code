# https://www.listendata.com/2024/01/4-ways-to-correct-grammar-with-python.html
# LanguageTool

import language_tool_python

mytext = """
I is testng grammar tool using python. It does not costt anythng.
"""

def grammarCorrector(text):
	tool = language_tool_python.LanguageTool('en-US')
	result = tool.correct(text)
	return result 

def grammarChecker(text):
	tool = language_tool_python.LanguageTool('en-US')
	result = tool.check(text)
	return result 

print("The original text is"+mytext)

output_data = grammarCorrector(mytext)
print("Grammar corrector: "+output_data)

check_data = grammarChecker(mytext)
print("Grammar checker: "+str(check_data))

print("Number of errors:"+str(len(check_data)))

# To see the detailed description of the first issue in the text
print("First issue:"+(str(check_data[0])))

# To see the replacements suggested by the tool for the first issue
print("Replacements suggested by the tool:"+(str(check_data[0].replacements)))

"""
Simplify Output of LanguageTool"
"""
def check_text(input_text):
	# Initialize LanguageTool instance
	tool = language_tool_python.LanguageTool('en-US')
	
	# Check for language errors in the input text
	matches = tool.check(input_text)
	
	# Initialize lists to store detected mistakes and their corrections
	mistakes = []
	corrections = []
	start_positions = []
	end_positions = []
	
	# Iterate through the detected language errors
	for rule in matches: 
		if len(rule.replacements) > 0: 
			start_positions.append(rule.offset)
			end_positions.append(rule.errorLength + rule.offset)
			mistakes.append(input_text[rule.offset: rule.errorLength + rule.offset])
			corrections.append(rule.replacements[0])
			
	return list(zip(mistakes,corrections))
	
check_text(mytext)

print("Checking: "+(str(check_text(mytext))))

"""
Supported Languages in LanguageTool
en-CA: Canadian English
en-AU: Australian English
en-NZ: New Zealand English
en-GB: British English
en-ZA: South African English
Further languages: ar, ast-ES, be-BY, br-FR, ca-ES, ca-ES-valencia, da-DK, de, de-AT, de-CH, de-DE, el-GR, en, en-AU, en-CA, en-GB, en-NZ, en-US, en-ZA, eo, es, es-AR, fa, fr, ga-IE, gl-ES, it, ja-JP, km-KH, nl, nl-BE, pl-PL, pt, pt-AO, pt-BR, pt-MZ, pt-PT, ro-RO, ru-RU, sk-SK, sl-SI, sv, ta-IN, tl-PH, uk-UA, zh-CN
"""

