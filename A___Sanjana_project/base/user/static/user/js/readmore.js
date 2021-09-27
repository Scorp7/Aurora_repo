function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }


  function myFunction() {
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("myBtn");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      btnText.innerHTML = "Read more";
      moreText.style.display = "none";
    } else {
      dots.style.display = "none";
      btnText.innerHTML = "Read less";
      moreText.style.display = "inline";
    }
  }


  





  



 





 


  

  











 


  
(function( $ ) {
	$.Shop = function( element ) {
		this.$element = $( element );
		this.init();
	};
	
	$.Shop.prototype = {
		init: function() {
		
		    // Properties
		
			this.cartPrefix = "Furniture-"; // Prefix string to be prepended to the cart's name in the session storage
			this.cartName = this.cartPrefix + "cart"; // Cart name in the session storage
			this.shippingRates = this.cartPrefix + "shipping-rates"; // Shipping rates key in the session storage
			this.total = this.cartPrefix + "total"; // Total key in the session storage
			this.storage = sessionStorage; // shortcut to the sessionStorage object
			
			
			this.$formAddToCart = this.$element.find( "form.add-to-cart" ); // Forms for adding items to the cart
			this.$formCart = this.$element.find( "#shopping-cart" ); // Shopping cart form
			this.$checkoutCart = this.$element.find( "#checkout-cart" ); // Checkout form cart
			this.$checkoutOrderForm = this.$element.find( "#checkout-order-form" ); // Checkout user details form
			this.$shipping = this.$element.find( "#sshipping" ); // Element that displays the shipping rates
			this.$subTotal = this.$element.find( "#stotal" ); // Element that displays the subtotal charges
			this.$shoppingCartActions = this.$element.find( "#shopping-cart-actions" ); // Cart actions links
			this.$updateCartBtn = this.$shoppingCartActions.find( "#update-cart" ); // Update cart button
			this.$emptyCartBtn = this.$shoppingCartActions.find( "#empty-cart" ); // Empty cart button
			this.$userDetails = this.$element.find( "#user-details-content" ); // Element that displays the user information
			this.$paypalForm = this.$element.find( "#paypal-form" ); // PayPal form
			
			
			this.currency = "&euro;"; // HTML entity of the currency to be displayed in the layout
			this.currencyString = "€"; // Currency symbol as textual string
			this.paypalCurrency = "EUR"; // PayPal's currency code
			this.paypalBusinessEmail = "yourbusiness@email.com"; // Your Business PayPal's account email address
			this.paypalURL = "https://www.sandbox.paypal.com/cgi-bin/webscr"; // The URL of the PayPal's form
			
			// Object containing patterns for form validation
			this.requiredFields = {
				expression: {
					value: /^([\w-\.]+)@((?:[\w]+\.)+)([a-z]){2,4}$/
				},
				
				str: {
					value: ""
				}
				
			};
			
			// Method invocation
			
			this.createCart();
			this.handleAddToCartForm();
			this.handleCheckoutOrderForm();
			this.emptyCart();
			this.updateCart();
			this.displayCart();
			this.deleteProduct();
			this.displayUserDetails();
			this.populatePayPalForm();
			
			
		},
		
		// Public methods
		
		// Creates the cart keys in the session storage
		
		createCart: function() {
			if( this.storage.getItem( this.cartName ) == null ) {
			
				var cart = {};
				cart.items = [];
			
				this.storage.setItem( this.cartName, this._toJSONString( cart ) );
				this.storage.setItem( this.shippingRates, "0" );
				this.storage.setItem( this.total, "0" );
			}
		},
		
		// Appends the required hidden values to the PayPal's form before submitting
		
		populatePayPalForm: function() {
			var self = this;
			if( self.$paypalForm.length ) {
				var $form = self.$paypalForm;
				var cart = self._toJSONObject( self.storage.getItem( self.cartName ) );
				var shipping = self.storage.getItem( self.shippingRates );
				var numShipping = self._convertString( shipping );
				var cartItems = cart.items; 
				var singShipping = Math.floor( numShipping / cartItems.length );
				
				$form.attr( "action", self.paypalURL );
				$form.find( "input[name='business']" ).val( self.paypalBusinessEmail );
				$form.find( "input[name='currency_code']" ).val( self.paypalCurrency );
				
				for( var i = 0; i < cartItems.length; ++i ) {
					var cartItem = cartItems[i];
					var n = i + 1;
					var name = cartItem.product;
					var price = cartItem.price;
					var qty = cartItem.qty;
					
					$( "<div/>" ).html( "<input type='hidden' name='quantity_" + n + "' value='" + qty + "'/>" ).
					insertBefore( "#paypal-btn" );
					$( "<div/>" ).html( "<input type='hidden' name='item_name_" + n + "' value='" + name + "'/>" ).
					insertBefore( "#paypal-btn" );
					$( "<div/>" ).html( "<input type='hidden' name='item_number_" + n + "' value='SKU " + name + "'/>" ).
					insertBefore( "#paypal-btn" );
					$( "<div/>" ).html( "<input type='hidden' name='amount_" + n + "' value='" + self._formatNumber( price, 2 ) + "'/>" ).
					insertBefore( "#paypal-btn" );
					$( "<div/>" ).html( "<input type='hidden' name='shipping_" + n + "' value='" + self._formatNumber( singShipping, 2 ) + "'/>" ).
					insertBefore( "#paypal-btn" );
					
				}
				
				
				
			}
		},
		
	

		// Delete a product from the shopping cart

		deleteProduct: function() {
			var self = this;
			if( self.$formCart.length ) {
				var cart = this._toJSONObject( this.storage.getItem( this.cartName ) );
				var items = cart.items;

				$( document ).on( "click", ".pdelete a", function( e ) {
					e.preventDefault();
					var productName = $( this ).data( "product" );
					var newItems = [];
					for( var i = 0; i < items.length; ++i ) {
						var item = items[i];
						var product = item.product;	
						if( product == productName ) {
							items.splice( i, 1 );
						}
					}
					newItems = items;
					var updatedCart = {};
					updatedCart.items = newItems;

					var updatedTotal = 0;
					var totalQty = 0;
					if( newItems.length == 0 ) {
						updatedTotal = 0;
						totalQty = 0;
					} else {
						for( var j = 0; j < newItems.length; ++j ) {
							var prod = newItems[j];
							var sub = prod.price * prod.qty;
							updatedTotal += sub;
							totalQty += prod.qty;
						}
					}

					self.storage.setItem( self.total, self._convertNumber( updatedTotal ) );
					self.storage.setItem( self.shippingRates, self._convertNumber( self._calculateShipping( totalQty ) ) );

					self.storage.setItem( self.cartName, self._toJSONString( updatedCart ) );
					$( this ).parents( "tr" ).remove();
					self.$subTotal[0].innerHTML = self.currency + " " + self.storage.getItem( self.total );
				});
			}
		},
		
		// Displays the shopping cart
		
		displayCart: function() {
			if( this.$formCart.length ) {
				var cart = this._toJSONObject( this.storage.getItem( this.cartName ) );
				var items = cart.items;
				var $tableCart = this.$formCart.find( ".shopping-cart" );
				var $tableCartBody = $tableCart.find( "tbody" );

				if( items.length == 0 ) {
					$tableCartBody.html( "" );	
				} else {
				
				
					for( var i = 0; i < items.length; ++i ) {
						var item = items[i];
						var product = item.product;
						var price = this.currency + " " + item.price;
						var qty = item.qty;
						var html = "<tr><td class='pname'>" + product + "</td>" + "<td class='pqty'><input type='text' value='" + qty + "' class='qty'/></td>";
					    	html += "<td class='pprice'>" + price + "</td><td class='pdelete'><a href='' data-product='" + product + "'>&times;</a></td></tr>";
					
						$tableCartBody.html( $tableCartBody.html() + html );
					}

				}

				if( items.length == 0 ) {
					this.$subTotal[0].innerHTML = this.currency + " " + 0.00;
				} else {	
				
					var total = this.storage.getItem( this.total );
					this.$subTotal[0].innerHTML = this.currency + " " + total;
				}
			} else if( this.$checkoutCart.length ) {
				var checkoutCart = this._toJSONObject( this.storage.getItem( this.cartName ) );
				var cartItems = checkoutCart.items;
				var $cartBody = this.$checkoutCart.find( "tbody" );

				if( cartItems.length > 0 ) {
				
					for( var j = 0; j < cartItems.length; ++j ) {
						var cartItem = cartItems[j];
						var cartProduct = cartItem.product;
						var cartPrice = this.currency + " " + cartItem.price;
						var cartQty = cartItem.qty;
						var cartHTML = "<tr><td class='pname'>" + cartProduct + "</td>" + "<td class='pqty'>" + cartQty + "</td>" + "<td class='pprice'>" + cartPrice + "</td></tr>";
					
						$cartBody.html( $cartBody.html() + cartHTML );
					}
				} else {
					$cartBody.html( "" );	
				}

				if( cartItems.length > 0 ) {
				
					var cartTotal = this.storage.getItem( this.total );
					var cartShipping = this.storage.getItem( this.shippingRates );
					var subTot = this._convertString( cartTotal ) + this._convertString( cartShipping );
				
					this.$subTotal[0].innerHTML = this.currency + " " + this._convertNumber( subTot );
					this.$shipping[0].innerHTML = this.currency + " " + cartShipping;
				} else {
					this.$subTotal[0].innerHTML = this.currency + " " + 0.00;
					this.$shipping[0].innerHTML = this.currency + " " + 0.00;	
				}
			
			}
		},
		
		// Empties the cart by calling the _emptyCart() method
		// @see $.Shop._emptyCart()
		
		emptyCart: function() {
			var self = this;
			if( self.$emptyCartBtn.length ) {
				self.$emptyCartBtn.on( "click", function() {
					self._emptyCart();
				});
			}
		},
		
		// Updates the cart
		
		updateCart: function() {
			var self = this;
		  if( self.$updateCartBtn.length ) {
			self.$updateCartBtn.on( "click", function() {
				var $rows = self.$formCart.find( "tbody tr" );
				var cart = self.storage.getItem( self.cartName );
				var shippingRates = self.storage.getItem( self.shippingRates );
				var total = self.storage.getItem( self.total );
				
				var updatedTotal = 0;
				var totalQty = 0;
				var updatedCart = {};
				updatedCart.items = [];
				
				$rows.each(function() {
					var $row = $( this );
					var pname = $.trim( $row.find( ".pname" ).text() );
					var pqty = self._convertString( $row.find( ".pqty > .qty" ).val() );
					var pprice = self._convertString( self._extractPrice( $row.find( ".pprice" ) ) );
					
					var cartObj = {
						product: pname,
						price: pprice,
						qty: pqty
					};
					
					updatedCart.items.push( cartObj );
					
					var subTotal = pqty * pprice;
					updatedTotal += subTotal;
					totalQty += pqty;
				});
				
				self.storage.setItem( self.total, self._convertNumber( updatedTotal ) );
				self.storage.setItem( self.shippingRates, self._convertNumber( self._calculateShipping( totalQty ) ) );
				self.storage.setItem( self.cartName, self._toJSONString( updatedCart ) );
				
			});
		  }
		},
		
		// Adds items to the shopping cart
		
		handleAddToCartForm: function() {
			var self = this;
			self.$formAddToCart.each(function() {
				var $form = $( this );
				var $product = $form.parent();
				var price = self._convertString( $product.data( "price" ) );
				var name =  $product.data( "name" );
				
				$form.on( "submit", function() {
					var qty = self._convertString( $form.find( ".qty" ).val() );
					var subTotal = qty * price;
					var total = self._convertString( self.storage.getItem( self.total ) );
					var sTotal = total + subTotal;
					self.storage.setItem( self.total, sTotal );
					self._addToCart({
						product: name,
						price: price,
						qty: qty
					});
					var shipping = self._convertString( self.storage.getItem( self.shippingRates ) );
					var shippingRates = self._calculateShipping( qty );
					var totalShipping = shipping + shippingRates;
					
					self.storage.setItem( self.shippingRates, totalShipping );
				});
			});
		},
		
		// Handles the checkout form by adding a validation routine and saving user's info into the session storage
		
		handleCheckoutOrderForm: function() {
			var self = this;
			if( self.$checkoutOrderForm.length ) {
				var $sameAsBilling = $( "#same-as-billing" );
				$sameAsBilling.on( "change", function() {
					var $check = $( this );
					if( $check.prop( "checked" ) ) {
						$( "#fieldset-shipping" ).slideUp( "normal" );
					} else {
						$( "#fieldset-shipping" ).slideDown( "normal" );
					}
				});
				
				self.$checkoutOrderForm.on( "submit", function() {
					var $form = $( this );
					var valid = self._validateForm( $form );
					
					if( !valid ) {
						return valid;
					} else {
						self._saveFormData( $form );
					}
				});
			}
		},
		
		// Private methods
		
		
		// Empties the session storage
		
		_emptyCart: function() {
			this.storage.clear();
		},
		
		/* Format a number by decimal places
		 * @param num Number the number to be formatted
		 * @param places Number the decimal places
		 * @returns n Number the formatted number
		 */
		 
		 
		
		_formatNumber: function( num, places ) {
			var n = num.toFixed( places );
			return n;
		},
		
		/* Extract the numeric portion from a string
		 * @param element Object the jQuery element that contains the relevant string
		 * @returns price String the numeric string
		 */
		
		
		_extractPrice: function( element ) {
			var self = this;
			var text = element.text();
			var price = text.replace( self.currencyString, "" ).replace( " ", "" );
			return price;
		},
		
		/* Converts a numeric string into a number
		 * @param numStr String the numeric string to be converted
		 * @returns num Number the number
		 */
		
		_convertString: function( numStr ) {
			var num;
			if( /^[-+]?[0-9]+\.[0-9]+$/.test( numStr ) ) {
				num = parseFloat( numStr );
			} else if( /^\d+$/.test( numStr ) ) {
				num = parseInt( numStr, 10 );
			} else {
				num = Number( numStr );
			}
			
			if( !isNaN( num ) ) {
				return num;
			} else {
				console.warn( numStr + " cannot be converted into a number" );
				return false;
			}
		},
		
		/* Converts a number to a string
		 * @param n Number the number to be converted
		 * @returns str String the string returned
		 */
		
		_convertNumber: function( n ) {
			var str = n.toString();
			return str;
		},
		
		/* Converts a JSON string to a JavaScript object
		 * @param str String the JSON string
		 * @returns obj Object the JavaScript object
		 */
		
		_toJSONObject: function( str ) {
			var obj = JSON.parse( str );
			return obj;
		},
		
		/* Converts a JavaScript object to a JSON string
		 * @param obj Object the JavaScript object
		 * @returns str String the JSON string
		 */
		
		
		_toJSONString: function( obj ) {
			var str = JSON.stringify( obj );
			return str;
		},
		
		
		/* Add an object to the cart as a JSON string
		 * @param values Object the object to be added to the cart
		 * @returns void
		 */
		
		
		_addToCart: function( values ) {
			var cart = this.storage.getItem( this.cartName );
			
			var cartObject = this._toJSONObject( cart );
			var cartCopy = cartObject;
			var items = cartCopy.items;
			items.push( values );
			
			this.storage.setItem( this.cartName, this._toJSONString( cartCopy ) );
		},
		
		/* Custom shipping rates calculation based on the total quantity of items in the cart
		 * @param qty Number the total quantity of items
		 * @returns shipping Number the shipping rates
		 */
		
		_calculateShipping: function( qty ) {
			var shipping = 0;
			if( qty >= 6 ) {
				shipping = 10;
			}
			if( qty >= 12 && qty <= 30 ) {
				shipping = 20;	
			}
			
			if( qty >= 30 && qty <= 60 ) {
				shipping = 30;	
			}
			
			if( qty > 60 ) {
				shipping = 0;
			}
			
			return shipping;
		
		},
		
		/* Validates the checkout form
		 * @param form Object the jQuery element of the checkout form
		 * @returns valid Boolean true for success, false for failure
		 */
		 
		 
		
		_validateForm: function( form ) {
			var self = this;
			var fields = self.requiredFields;
			var $visibleSet = form.find( "fieldset:visible" );
			var valid = true;
			
			form.find( ".message" ).remove();
			
		  $visibleSet.each(function() {
			
			$( this ).find( ":input" ).each(function() {
				var $input = $( this );
				var type = $input.data( "type" );
				var msg = $input.data( "message" );
				
				if( type == "string" ) {
					if( $input.val() == fields.str.value ) {
						$( "<span class='message'/>" ).text( msg ).
						insertBefore( $input );
						
						valid = false;
					}
				} else {
					if( !fields.expression.value.test( $input.val() ) ) {
						$( "<span class='message'/>" ).text( msg ).
						insertBefore( $input );
						
						valid = false;
					}
				}
				
			});
		  });
			
			return valid;
		
		},
		
		/* Save the data entered by the user in the ckeckout form
		 * @param form Object the jQuery element of the checkout form
		 * @returns void
		 */
		
		
		_saveFormData: function( form ) {
			var self = this;
			var $visibleSet = form.find( "fieldset:visible" );
			
			$visibleSet.each(function() {
				var $set = $( this );
				if( $set.is( "#fieldset-billing" ) ) {
					var name = $( "#name", $set ).val();
					var email = $( "#email", $set ).val();
					var city = $( "#city", $set ).val();
					var address = $( "#address", $set ).val();
					var zip = $( "#zip", $set ).val();
					var country = $( "#country", $set ).val();
					
					self.storage.setItem( "billing-name", name );
					self.storage.setItem( "billing-email", email );
					self.storage.setItem( "billing-city", city );
					self.storage.setItem( "billing-address", address );
					self.storage.setItem( "billing-zip", zip );
					self.storage.setItem( "billing-country", country );
				} else {
					var sName = $( "#sname", $set ).val();
					var sEmail = $( "#semail", $set ).val();
					var sCity = $( "#scity", $set ).val();
					var sAddress = $( "#saddress", $set ).val();
					var sZip = $( "#szip", $set ).val();
					var sCountry = $( "#scountry", $set ).val();
					
					self.storage.setItem( "shipping-name", sName );
					self.storage.setItem( "shipping-email", sEmail );
					self.storage.setItem( "shipping-city", sCity );
					self.storage.setItem( "shipping-address", sAddress );
					self.storage.setItem( "shipping-zip", sZip );
					self.storage.setItem( "shipping-country", sCountry );
				
				}
			});
		}
	};
	
	$(function() {
		var shop = new $.Shop( "#site" );
	});

})( jQuery );





$('.add-to-cart').on('click', (e) => {
  addToCart(e.currentTarget)
})

const addToCart = (product) => {
  const productId = $(product).attr('productId');
  const isAlreadyInCart = $.grep(productsInCart, el => {return el.id == productId}).length;

  if (isAlreadyInCart) {
    $.each(storageData, (i, el) => {
      if (productId == el.id) {
        el.itemsNumber += 1;
      }
    })
  } else {
    const newProduct = {
      id: Number(productId),
      itemsNumber: 1
    }

    storageData.push(newProduct);
  }

  updateCart();
  updateProductList();
}








































$('.add-to-cart').on('click', (e) => {
	addToCart(e.currentTarget)
  })
  
  const addToCart = (product) => {
	const productId = $(product).attr('productId');
	const isAlreadyInCart = $.grep(productsInCart, el => {return el.id == productId}).length;
  
	if (isAlreadyInCart) {
	  $.each(storageData, (i, el) => {
		if (productId == el.id) {
		  el.itemsNumber += 1;
		}
	  })
	} else {
	  const newProduct = {
		id: Number(productId),
		itemsNumber: 1
	  }
  
	  storageData.push(newProduct);
	}
  
	updateCart();
	updateProductList();
  }
  [
	{
	  "id": 1,
	  "category": "jeans",
	  "name": "Ripped jeans",
	  "image": "https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/11.jpg",
	  "size": "XL",
	  "color": "blue",
	  "price": 20.99
	},
	{
	  "id": 2,
	  "category": "jeans",
	  "name": "Boyfriend jeans",
	  "image": "https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/10.jpg",
	  "size": "S",
	  "color": "blue",
	  "price": 24.99
	},
	{
	  "id": 3,
	  "category": "shirts",
	  "name": "Ripped sweatshirt",
	  "image": "https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/7.jpg",
	  "size": "XL",
	  "color": "white",
	  "price": 29.99
	},
	{
	  "id": 4,
	  "category": "jackets",
	  "name": "Denim Jacket",
	  "image": "https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/15.jpg",
	  "size": "M",
	  "color": "grey",
	  "price": 40.99
	},
	{
	  "id": 5,
	  "category": "shirts",
	  "name": "Longsleeve",
	  "image": "https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/8.jpg",
	  "size": "L",
	  "color": "black",
	  "price": 120.99
	}
  ]


  $(document).ready(() => {
	let storageData = [];
  
	$.get("product.json", (res) => {
	  productList = res;
  
	  const isStorageEmpty = Cookies.getStorage('cart').length === 0;
  
	  if (!isStorageEmpty) {
		storageData = Cookies.getStorage('cart');
	  }
  
	  updateCart();
	  buildProductList();
	  buildDropdownCart();
	  bindProductEvents();
	});
  });


  const updateCart = () => {
	Cookies.setStorage('cart', storageData);
	productsInCart = [];
  
	parseStorageDataWithProduct();
	updatePill();
	updateTotalAmount();
  }
  
  const parseStorageDataWithProduct = () => {
	$.each(storageData, (i, el) => {
	  const id = el.id;
	  const itemsNumber = el.itemsNumber;
  
	  $.each(productList, (i, el) => {
		if (id == el.id) {
		  el.itemsNumber = itemsNumber;
		  productsInCart.push(el)
		}
	  });
	});
  }
  
  const updatePill = () => {
	let itemsInCart = 0;
  
	$.each(productsInCart, (i, el) => {
	  itemsInCart += el.itemsNumber;
	});
  
	$('.badge-pill').html(itemsInCart);
  }
  
  const updateTotalAmount = () => {
	let total = 0;
	const shippingCost = 0;
	let summary = (total + shippingCost).toFixed(2);
  
	$.each(productsInCart, (i, el) => {
	  total += el.itemsNumber * el.price;
	});
  
	$('#total-price').html(`$${total.toFixed(2)}`);
	$('#shipping-price').html(shippingCost === 0 ? 'Free' : `$${shippingCost}`);
	$('#summary').html(`$${summary}`);
  }

  const dropdownProductsTemplate = (product) => {
	return `
	  <div id="${product.id}-dropdown" class="product row">
		<div class="col-4 px-2">
		  <div class="view zoom overlay z-depth-1 rounded mb-md-0">
			<img class="img-fluid w-100" src="${product.image}" alt="Sample">
		  </div>
		</div>
		<div class="col-5 px-2">
		  <span>${product.name}</span>
		  <p class="mb-0"><span><strong class="price">$${(product.price * product.itemsNumber).toFixed(2)}</strong></span></p>
		</div>
		<div class="col-2 pl-0 pr-2">
		  <a href="#!" type="button" class="remove-product"><i class="fas fa-trash-alt"></i></a>
		</div>
	  </div>
	  </div>
	  <hr class="mb-4">
	`
  }
  
  const productsTemplate = (product) => {
	return `
	  <div id="${product.id}" class="product row mb-4">
		<div class="col-md-5 col-lg-3 col-xl-3">
		  <div class="view zoom overlay z-depth-1 rounded mb-3 mb-md-0">
			<img class="img-fluid w-100" src="${product.image}" alt="Sample">
			<a href="#!">
			  <div class="mask waves-effect waves-light">
				<img class="img-fluid w-100" src="${product.image}">
				<div class="mask rgba-black-slight waves-effect waves-light"></div>
			  </div>
			</a>
		  </div>
		</div>
		<div class="col-md-7 col-lg-9 col-xl-9">
		  <div>
			<div class="d-flex justify-content-between">
			  <div>
				<h5>${product.name}</h5>
				<p class="mb-3 text-muted text-uppercase small">${product.category} - ${product.color}</p>
				<p class="mb-2 text-muted text-uppercase small">Color: ${product.color}</p>
				<p class="mb-3 text-muted text-uppercase small">Size: ${product.size}</p>
			  </div>
			  <div>
				<div class="def-number-input number-input safari_only mb-0 w-100">
				  <button class="minus decrease"></button>
				  <input class="quantity" min="0" name="quantity" value="${product.itemsNumber}" type="number">
				  <button class="plus increase"></button>
				</div>
				<small id="passwordHelpBlock" class="form-text text-muted text-center"> (Note, 1 piece) </small>
			  </div>
			</div>
			<div class="d-flex justify-content-between align-items-center">
			  <div>
				<a href="#!" type="button" class="remove-product card-link-secondary small text-uppercase mr-3"><i class="fas fa-trash-alt mr-1"></i> Remove item </a>
				<a href="#!" type="button" class="card-link-secondary small text-uppercase"><i class="fas fa-heart mr-1"></i> Move to wish list </a>
			  </div>
			  <p class="mb-0"><span><strong class="price">$${(product.price * product.itemsNumber).toFixed(2)}</strong></span></p>
			</div>
		  </div>
		</div>
	  </div>
	  <hr class="mb-4">
	`
  };

  const buildProductList = () => {
	$.each(productsInCart, (i, el) => {
	  const product = renderProducts(el)
	  $('#product-list').append(product);
	})
  }
  
  const buildDropdownCart = () => {
	$.each(productsInCart, (i, el) => {
	  const product = renderDropdownProducts(el);
	  $('#dropdown-cart').append(product)
	})
  }
  
  const bindProductEvents = () => {
	$('button.increase').on('click', (e) => {
	  increaseProductQuantity(e.currentTarget);
	});
  
	$('button.decrease').on('click', (e) => {
	  subtractProductQuantity(e.currentTarget);
	});
  
	$('a.remove-product').on('click', (e) => {
	  removeProduct(e.currentTarget);
	});
  }

  const increaseProductQuantity = (product) => {
	const productId = $(product).parents('.product').get(0).id
	const price = $.grep(productsInCart, el => { return el.id == productId })[0].price;
  
	$.each(storageData, (i, el) => {
	  if (el.id == productId) {
		el.itemsNumber += 1
		$(product).siblings('.quantity').val(el.itemsNumber);
		$(`#${productId}`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
		$(`#${productId}-dropdown`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
	  }
	});
  
	updateCart();
  }
  
  const subtractProductQuantity = (product) => {
	const productId = $(product).parents('.product').get(0).id
	const price = $.grep(productsInCart, el => { return el.id == productId })[0].price;
	let itemsInCart = $.grep(productsInCart, el => { return el.id == productId })[0].itemsNumber;
  
	if (itemsInCart > 0 ) {
	  storageData.map( el => {
		if (el.id == productId) {
		  el.itemsNumber -= 1
		  $(product).siblings('.quantity').val(el.itemsNumber)
		  $(`#${productId}`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
		  $(`#${productId}-dropdown`).find('.price').html(`$${(price * el.itemsNumber).toFixed(2)}`);
		}
	  });
  
	  updateCart();
	};
  }
  
  const removeProduct = (product) => {
	const productId = $(product).parents('.product').get(0).id
  
	storageData = $.grep(storageData, (el, i) => {
	  return el.id != productId
	});
  
	updateCart();
	updateProductList();
  }
  const updateProductList = () => {
	$('#product-list').empty();
	buildProductList();
	$('#dropdown-cart').empty();
	buildDropdownCart();
	bindProductEvents();
  }



  