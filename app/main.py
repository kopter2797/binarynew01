from flask import Flask, render_template, request
from quicksort import quicksort_ascending, quicksort_descending
from binary_search import binary_search

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'num_count' in request.form:
            num_count = int(request.form['num_count'])
            numbers = [int(request.form[f'num{i+1}']) for i in range(num_count)]
            choice = request.form['choice']
            
            if choice == '1':
                sorted_numbers = quicksort_ascending(numbers)
                reverse = False
            elif choice == '2':
                sorted_numbers = quicksort_descending(numbers)
                reverse = True
            
            sorted_numbers_str = ', '.join(map(str, sorted_numbers))
            return render_template('index.html', sorted_numbers=sorted_numbers_str, reverse=reverse)
        
        elif 'target' in request.form:
            sorted_numbers = list(map(int, request.form['sorted_numbers'].split(', ')))
            target = int(request.form['target'])
            reverse = request.form.get('reverse') == 'True'
            index = binary_search(sorted_numbers, target, reverse)
            result = f"พบ {target} ที่ตำแหน่ง {index}" if index != -1 else f"ไม่พบ {target}"
            
            sorted_numbers_str = ', '.join(map(str, sorted_numbers))
            return render_template('index.html', sorted_numbers=sorted_numbers_str, result=result)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)