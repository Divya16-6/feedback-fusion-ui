import streamlit as st
from service.productApi import fetch_product_details
from service.feedbackApi import addUserFeedback
from model import FeedbackModel


st.markdown(
    "<h2 style='text-align: center;'>Your Feedback is important for us 😎</h2>",
    unsafe_allow_html=True
)
st.divider()

result = fetch_product_details()
st.subheader("Product Details")


selectedproduct = st.selectbox(
    "Select the product to provide your feedback!!",
    options=result,
    format_func=lambda x: x["productName"],
    index=None,
    accept_new_options=True,
    placeholder= "Your feedback makes us to improve",
    key="product"
)


feedback = st.text_input(
    "Provide your feedback here!",
    label_visibility="visible",
    placeholder= "Each and every feedback is valued here",
    key="feedback"
)


res = st.button("Submit 😌", use_container_width=True, disabled=not (selectedproduct and feedback))
if res:
    data = FeedbackModel.userFeedback(
        productId= selectedproduct["productId"],
        text= feedback
    )
    result = addUserFeedback(data)
    if result["sentiment"] == "Positive":
        st.success(f"🎉 {result['message']}")
    elif result["sentiment"] == "Negative":
        st.error(f"😞 {result['message']}")