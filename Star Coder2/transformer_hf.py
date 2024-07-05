from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("bigcode/starcoder2-7b", device_map="auto")
tokenizer = AutoTokenizer.from_pretrained("bigcode/starcoder2-7b")

prompt = "def print_hello_world():"

model_inputs = tokenizer([prompt], return_tensors="pt")

generated_ids = model.generate(**model_inputs, max_new_tokens=10, do_sample=False)
tokenizer.batch_decode(generated_ids)[0]