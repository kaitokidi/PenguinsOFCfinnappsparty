package com.webs.asciipenguins.finappspenguins;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;


public class WebViewActivity extends Activity {

    private WebView webView;

    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.webview);

        webView = (WebView) findViewById(R.id.webView1);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.loadUrl("http://192.168.10.17/actions");

        //Log.i("idea", webView.toString());
        webView.setScrollBarStyle(View.SCROLLBARS_INSIDE_INSET);


        //String customHtml = "<html><body><h1>Hello, WebView</h1></body></html>";

       //webView.loadData(customHtml, "text/html", "UTF-8");

    }

}