import pickle
import torch
import vanilla
CONTEXT_LENGTH = 100

dataset = ''
with open('dataset.txt', 'r', encoding='utf-8') as f:
    dataset = f.read()
vocab = sorted(list(set(dataset)))

def predict_generate(seed_text,length):
    model = pickle.load(open('10_26000_0.21806052327156067.pkl', 'rb'))
    char_to_id = {k: v for v, k in enumerate(vocab)}
    id_to_char = {k: v for k, v in enumerate(vocab)}
    with torch.no_grad():  # Tắt tính toán gradient
        # Chuyển đổi seed_text thành dạng số nguyên sử dụng char_to_id
        seed_text = [char_to_id[c] for c in seed_text]
        
        generated_text = seed_text.copy()
        
        # Dự đoán và thêm từng ký tự tiếp theo vào generated_text
        for _ in range(length):
            input_sequence = torch.tensor(generated_text[-CONTEXT_LENGTH:])  # Lấy CONTEXT_LENGTH ký tự gần nhất
            vals = model.forward(input_sequence)
            predicted_id = torch.argmax(vals['o_timesteps'][-1]).item()  # Chọn ký tự có xác suất cao nhất
            generated_text.append(predicted_id)
        # Chuyển đổi lại dạng ký tự và trả về văn bản được tạo ra
        generated_text = [id_to_char[c] for c in generated_text]
        generated_text = ''.join(generated_text)    
    return generated_text


 

