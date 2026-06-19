from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "facebook/nllb-200-distilled-600M"

print("Loading Translation Model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

print("Model Loaded!")

language_codes = {
    "english": "eng_Latn",
    "hindi": "hin_Deva",
    "malayalam": "mal_Mlym",
    "tamil": "tam_Taml",
    "french": "fra_Latn",
    "arabic": "arb_Arab",
    "korean": "kor_Hang",
    "bengali": "ben_Beng",
    "urdu": "urd_Arab",
    "russian": "rus_Cyrl",
    
    
}


def translate_text(text, source_lang, target_lang):

    src_code = language_codes[source_lang.lower()]
    tgt_code = language_codes[target_lang.lower()]

    tokenizer.src_lang = src_code

    inputs = tokenizer(
        text,
        return_tensors="pt"
    )

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(tgt_code),
        max_length=100
    )

    translated_text = tokenizer.batch_decode(
        translated_tokens,
        skip_special_tokens=True
    )[0]

    return translated_text