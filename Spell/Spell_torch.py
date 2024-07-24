import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import nltk
from nltk.tokenize import word_tokenize

class SpellCorrectionDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text, label = self.data[idx]
        tokens = word_tokenize(text)
        tokens = [token.lower() for token in tokens]
        return {
            'input_ids': torch.tensor([tokens]),
            'attention_mask': torch.tensor([[1] * len(tokens)]),
            'labels': torch.tensor([label])
        }

class TransformerModel(nn.Module):
    def __init__(self):
        super(TransformerModel, self).__init__()
        self.transformer = nn.Transformer(d_model=512, nhead=8)
        self.fc = nn.Linear(512, 1)

    def forward(self, input_ids, attention_mask):
        output = self.transformer(input_ids, attention_mask)
        output = self.fc(output[:, 0, :])
        return output

# Load and preprocess the data
dataset = SpellCorrectionDataset(data)
dataloader = DataLoader(dataset, batch_size=32)

# Initialize the model, optimizer, and loss function
model = TransformerModel()
optimizer = optim.Adam(model.parameters(), lr=1e-4)
loss_fn = nn.CrossEntropyLoss()

# Train the model
for epoch in range(5):
    for batch in dataloader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        optimizer.zero_grad()
        output = model(input_ids, attention_mask)
        loss = loss_fn(output, labels)
        loss.backward()
        optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')

# Use the trained model for inference
def correct_misspelling(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens]
    input_ids = torch.tensor([tokens])
    attention_mask = torch.tensor([[1] * len(tokens)])
    output = model(input_ids, attention_mask)
    _, predicted = torch.max(output, dim=1)
    return predicted[0].item()

print(correct_misspelling('teh'))  # 0 (index of the correct word in the vocabulary)