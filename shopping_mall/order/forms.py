from django import forms

class OrderForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required':'수량을 입력해주세요.'
        }, label="수량")
    
    product = forms.IntegerField(
        error_messages={
            'required':'상품을 입력해주세요.'
        },
    label="상품", widget=forms.HiddenInput
    )