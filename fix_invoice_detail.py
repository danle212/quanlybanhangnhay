from pathlib import Path
import re
path = Path(r'c:\Users\HUYPC\OneDrive\Documents\Danny\webapp\quanlybanhangnhay\index.html')
text = path.read_text(encoding='utf-8')
old = '''\t\t\t\t<tr id="det-${inv.id}" class="detail-row" style="display:none;"><td colspan="5">
\t\t\t\t\t<table style="width:95%; margin:10px auto; border:1px solid #444;">
\t\t\t\t\t\t<tbody>
\t\t\t\t\t\t\t${inv.items.map(it => {
\t\t\t\t\t\t\tconst price = parseFloat(it[4]) || (parseFloat(it[6]) / parseFloat(it[5])) || 0;

\t\t\t\t\t\t\treturn `<tr data-price="${price}" data-cust-name="${custName}" data-cust-points="${custPoints}">
\t\t\t\t\t\t\t\t<td>${it[2]}</td>
\t\t\t\t\t\t\t\t<td>${it[5]}</td>
\t\t\t\t\t\t\t\t<td>${parseFloat(it[6]).toLocaleString()}</td>
\t\t\t\t\t\t\t</tr>`;
'''
new = '''\t\t\t\t<tr id="det-${inv.id}" class="detail-row" style="display:none;"><td colspan="5">
\t\t\t\t\t<div style="padding: 12px 14px; background: #1a1a1a; margin-bottom: 12px; border-radius: 8px; border: 1px solid #333;">
\t\t\t\t\t\t<div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; color:#fff;">
\t\t\t\t\t\t\t<div><strong>Khách hàng:</strong> ${custName}</div>
\t\t\t\t\t\t\t<div><strong>Tổng tiền:</strong> ${inv.total.toLocaleString()} đ</div>
\t\t\t\t\t\t\t<div><strong>Điểm tích lũy:</strong> ${custPoints.toLocaleString()}</div>
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
\t\t\t\t\t<table style="width:95%; margin:0 auto 10px; border:1px solid #444;">
\t\t\t\t\t\t<thead>
\t\t\t\t\t\t\t<tr style="background:#252525; color:#fff;">
\t\t\t\t\t\t\t\t<th style="padding: 10px; text-align:left;">Sản phẩm</th>
\t\t\t\t\t\t\t\t<th style="padding: 10px; text-align:right;">Giá</th>
\t\t\t\t\t\t\t\t<th style="padding: 10px; text-align:center;">SL</th>
\t\t\t\t\t\t\t\t<th style="padding: 10px; text-align:right;">Thành tiền</th>
\t\t\t\t\t\t\t</tr>
\t\t\t\t\t\t</thead>
\t\t\t\t\t\t<tbody>
\t\t\t\t\t\t\t${inv.items.map(it => {
\t\t\t\t\t\t\tconst price = parseFloat(it[4]) || (parseFloat(it[6]) / parseFloat(it[5])) || 0;

\t\t\t\t\t\t\treturn `<tr data-price="${price}" data-cust-name="${custName}" data-cust-points="${custPoints}">
\t\t\t\t\t\t\t\t<td style="padding: 10px;">${it[2]}</td>
\t\t\t\t\t\t\t\t<td style="padding: 10px; text-align:right;">${price.toLocaleString()} đ</td>
\t\t\t\t\t\t\t\t<td style="padding: 10px; text-align:center;">${it[5]}</td>
\t\t\t\t\t\t\t\t<td style="padding: 10px; text-align:right;">${parseFloat(it[6]).toLocaleString()} đ</td>
\t\t\t\t\t\t\t</tr>`;
'''
if old not in text:
    raise RuntimeError('Old block not found')
text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
print('DONE')
