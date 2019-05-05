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
import org.springframework.web.bind.annotation.RestController;

import com.jmprueba.otherhwrestapi.entity.Category;
import com.jmprueba.otherhwrestapi.service.CategoryService;

@RestController
public class CategoryRest {

	@Autowired
	CategoryService categoryService;

	@GetMapping("/api/v1/categories")
	public Page<Category> getAllCategories(Pageable pageable) {
		return categoryService.findAll(pageable);
	}

	@GetMapping("/api/v1/categories/findByName/{name}")
	public List<Category> getAllCategories(@PathVariable String name) {
		return categoryService.findBydName(name);
	}

	
	@PostMapping("/api/v1/categories")
	public Category createCategory(@Valid @RequestBody Category category) {
		return categoryService.save(category);
	}

	@PutMapping("/api/v1/categories/{categoryId}")
	public Category updateCategory(@PathVariable Long categoryId, @Valid @RequestBody Category category) {
		Category categoryUpdated = categoryService.updateCategory(categoryId, category);
		if (categoryUpdated == null)
			throw new ResourceNotFoundException("categoryId " + categoryId + " not found");
		return categoryUpdated;
	}

	@DeleteMapping("/api/v1/categories/{categoryId}")
	public ResponseEntity<?> deleteCategory(@PathVariable Long categoryId) {

		if (!categoryService.deleteCategory(categoryId))
			throw new ResourceNotFoundException("categoryId " + categoryId + " not found");

		return ResponseEntity.ok().build();

	}

	@GetMapping("/api/v1/categories/count")
	public Long countCategory() {
		return categoryService.countCategory();
	}

}
