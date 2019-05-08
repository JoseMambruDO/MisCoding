package com.jmprueba.otherhwrestapi.api;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.rest.webmvc.ResourceNotFoundException;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.jmprueba.otherhwrestapi.entity.Category;
import com.jmprueba.otherhwrestapi.entity.Product;
import com.jmprueba.otherhwrestapi.service.ProductService;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;

@RestController
@Api("Product RestAPI")
@RequestMapping("/api/v1/products")
public class ProductRest {

	@Autowired
	ProductService productService;

	@ApiOperation(value = "View a list of available products", response = Page.class)

	@ApiResponses(value = { @ApiResponse(code = 200, message = "Successfully retrieved list"),
			@ApiResponse(code = 401, message = "You are not authorized to view the resource"),
			@ApiResponse(code = 403, message = "Accessing the resource you were trying to reach is forbidden"),
			@ApiResponse(code = 404, message = "The resource you were trying to reach is not found") }

	)
	@GetMapping
	public Page<Product> getAllProducts(Pageable pageable) {
		return productService.findAll(pageable);
	}

	@ApiOperation(value = "Get a list of products", response = List.class)

	@GetMapping("findByName/{name}")
	public List<Product> findBydName(@PathVariable String name) {
		return productService.findBydName(name);
	}
	
	@GetMapping("findByID/{id}")
	public Product getProductByID(@PathVariable Long id ){
		return productService.findById(id);
	}

	@ApiOperation(value = "Create a new product", response = Product.class)

	@PostMapping
	public Product createProduct(@Valid @RequestBody Product product) {
		return productService.save(product);
	}

	@ApiOperation(value = "Edit a product", response = Product.class)

	@PutMapping("{id}")
	public Product updateProduct(@PathVariable Long productId, @Valid @RequestBody Product product) {
		Product productUpdated = productService.updateProduct(productId, product);
		if (productUpdated == null)
			throw new ResourceNotFoundException("Product Id " + productId + " not found");
		return productUpdated;
	}

	@ApiOperation(value = "Delete a product")

	@DeleteMapping("{id}")
	public String deleteProduct(@PathVariable Long id) {

		if (!productService.deleteProduct(id))
			throw new ResourceNotFoundException("Product Id " + id + " not found");

		return String.format("Product id:%d was deleted.", id);
		

	}

	@ApiOperation(value = "Count avaiable products")

	@GetMapping("/api/v1/products/count")
	public Long countProduct() {
		return productService.countProduct();
	}

}
