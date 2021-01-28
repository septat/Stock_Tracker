import streamlit as st
import pandas as pd
import yfinance as yf
import yahoo_fin.stock_info as si


# Plotting Function
def price_history(stock_info, symbol):
    st.write("Below is the price history based on selected criteria")
    st.line_chart(stock_info, 0, 0, True)
    if st.button("Show Extended Information"):
        quote_table = si.get_quote_table(symbol, dict_result=False)
        st.dataframe(quote_table)


def main():

    ### Title ###
    st.title('Stock Tracker')

    st.markdown("""This project aims to present any ***given stock*** currently existing on the NYSE with information on opening and closing price, its price to expense ratio, and a graph charting its performance.
    \n **Python libraries:** pandas, streamlit, numpy, matplotlib, yfinance""")

    # SIDEBAR USER INPUT AREA
    st.sidebar.header("User Input")
    stock_symbol = st.sidebar.text_input("Please Insert Valid Stock Symbol(s)")
    options = st.sidebar.multiselect(
        "Metrics", ["Open", "High", "Low", "Close", "Volume"]
    )

    if st.sidebar.button("Check"):
        try:
            data = yf.download(
                tickers=stock_symbol[:10],
                period="ytd",
                interval="1d",
                group_by='ticker',
                auto_adjust=True,
                prepost=True,
                threads=True,
                proxy=None
            )
        except:
            st.write("Error: Please try again with a valid existing stock")

        data
        #df = pd.DataFrame(data[options])
        #st.dataframe(df)
        #if "Volume" in options:
        #    df = df.drop(columns = "Volume")
        #price_history(df, stock_symbol)

# def price_plot(symbol):
#   df = pd.DataFrame(data[symbol].Close)
#   df['Date'] = df.index
#   plt.title(stock_symbol, fontweight='bold')
#   plt.xlabel('Date', fontweight='bold')
#   plt.ylabel('Closing Price', fontweight='bold')
#   return st.pyplot()

# if st.button('Show Plots'):
#     st.header('Stock Closing Price')
#     price_plot(stock_symbol)


# THE SIDEBAR CANT BE IMPLEMENTED FOR LACK OF CONCRETE IDEA OF IMPLEMENTATION
#st.sidebar.header('User Input Features')


# CSV FILE DOWNLOAD #
# def filedownload(df):
#     csv = df.to_csv(index=False)
#     # strings <-> bytes conversions
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
#     return href

main()
