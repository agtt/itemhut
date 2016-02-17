% include('global/header.tpl')

<div class="off-canvas-wrapper">

  <div class="off-canvas-wrapper-inner" data-off-canvas-wrapper>

% include('global/top_bar.tpl')
% include('global/top_nav.tpl')


    <!-- original content goes in this container -->

    <div class="off-canvas-content" data-off-canvas-content>

      <div class="expanded row">
      	   <div class="medium-2 columns">
	   	<ul class="vertical menu">
			<li>
			Add Product
			</li>
		</ul>
	   </div>

      	   <div class="medium-10 columns">
	   % if new_sku:
	   <p>Added {{new_sku}}</p>
	   % end
	   <form action="/products/add-product" method="POST">

	   <div class="row">
	   <div class="medium-2 columns">
	   <label>Sku
	   	  <input type="text" name="sku" required="required">
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>UPC
	   	  <input type="text" name="upc">
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>SKU Type
	   <select name="sku-type">
	   % for item in sku_types:
	     <option value="{{item[0]}}">{{item[0]}}</option>
	   % end
	   </select>
	   </label>
	   </div>

	   <div class="medium-2 columns">
	   <label>Product Name
	   	  <input type="text" name="product_name">
	   </label>
	   </div>

	   <div class="medium-4 columns">
	   </div>

	   </div>
	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Product Description
	   		  <textarea name="product-description"></textarea>
           </label>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	   </div>

	   % for item in ["One", "Two", "Three", "Four", "Five"]:
	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Bullet {{item}}
		<input type="text" name="bullet-{{item.lower()}}">
	   </label>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	   </div>
	   % end

	   <div class="row">
	   <div class="medium-6 columns">
	   <label>Main Image
		<input type="text" name="main-image">
	   </label>
	   <div class="medium-6 columns">
 	   </div>
	   </div>
	   </div>

	   % for item in ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve"]:
	   <div class="row">
	   <div class="medium-6 columns">
	   
	   <label>Image {{item}}
	   <input type="text" name="image-{{item}}">
	   </label>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	   </div>
	   % end

	   <div class="row">
	   <div class="medium-6 columns">

	   <label>Swatch Image
		<input type="text" name="swatch-image">
	   </label>
	   <div class="medium-6 columns">
	   </div>
	   </div>
	   </div>

	   <div class="row">
	   <div class="medium-2 columns">
	   <input type="submit" class="button" value="Add Product" name="add-product">
	   </div>
	   </div>

	   </form>
	   </div>
      </div>

    </div>
  <!-- close wrapper, no more content after this -->

  </div>

</div>

% include('global/end_body.tpl')