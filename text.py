import streamlit as st


from google import genai
st.title("Text Translator")

client = genai.Client(api_key="..............")

def answer(prompt,language):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[f"""You are expert in translating,please translate the file {prompt} into the language {language}
                  follow these rules:
                  -Do not give any extra lines
                  -Give a separate heading 'Successfully Translated' in big font
                  -not give input
                  -also detect the input language
                  """]
    )
    return response

content=st.text_area("Enter your Text")
language=st.selectbox("Enter the language Which you want to translate this text",
                      ["Hindi","French","Chinees","Arbic"]
                      )
if st.button("Generate"):
       if content:
        with st.spinner("Translating..."):
            prompt=content
            result=answer(prompt,language)
            st.write(result.text)
       else:
           st.warning("Please uplode your text ⚠")     
   