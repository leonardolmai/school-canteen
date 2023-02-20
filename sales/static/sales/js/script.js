const cart = document.getElementById('cart');
const totalDiv = document.getElementById('total');
let shoppingCart = [];

class Product {
  constructor(id, price, quantity) {
    this.id = id;
    this.price = price;
    this.quantity = quantity;
  }
}

function add_cart() {
  const select = document.getElementById('select-product');
  const id = select.options[select.selectedIndex].value;
  const price = parseFloat(JSON.parse(document.getElementById(id).textContent));
  const quantity = parseInt(document.getElementById('quantity').value);
  const product = shoppingCart.find((item => item.id == id));

  if (product) {
    product.quantity += quantity;
    const quantityInput = document.getElementById(id + 'q');
    const totalTd = document.getElementById(id + 't');
    totalTd.innerText = `R$${(product.quantity * product.price).toFixed(2)}`;
    quantityInput.setAttribute('value', product.quantity);

  } else {
    let new_product = new Product(id, price, quantity);
    shoppingCart.push(new_product);
    const name = select.options[select.selectedIndex].textContent;

    cart.innerHTML += `
      <tr class="register-sale__tr" id="${id}row">
        <td scope="row"><input type="hidden" value="${name}" name="products">${name}</td>
        <td>R$${price.toFixed(2)}</td>
        <td><input type="number" class="form-control register-sale__table-input" value="${quantity}" id="${id}q" name="quantities" onchange="modifyQuantity(this)" min=1></td>
        <td id="${id}t">R$${(price * quantity).toFixed(2)}</td>
        <td>
          <a class="btn" id="remove-cart">
            <img src="./../../../static/img/remove.svg" alt="Ícone remover" class="icon-remove" onclick="remove_cart(this)" id="${id}">
          </a>
        </td>
      </tr>`;
  }

  totalDiv.innerText = `R$${getTotal().toFixed(2)}`;
}

function remove_cart(element) {
  const row = document.getElementById(element.id + 'row');
  shoppingCart = shoppingCart.filter((item => item.id !== element.id));
  row.remove();
  totalDiv.innerText = `R$${getTotal().toFixed(2)}`;
}

function modifyQuantity(element) {
  const id = element.id.slice(0, -1);
  const quantityInput = element;
  const product = shoppingCart.find((item => item.id == id));
  product.quantity = quantityInput.value;
  quantityInput.setAttribute('value', product.quantity);
  const totalTd = document.getElementById(id + 't');
  totalTd.innerText = `R$${(product.quantity * product.price).toFixed(2)}`;
  totalDiv.innerText = `R$${getTotal().toFixed(2)}`;
}

function getTotal() {
  let total = 0;
  shoppingCart.forEach((product) => {
    total += product.price * product.quantity;
  })
  return total;
}
