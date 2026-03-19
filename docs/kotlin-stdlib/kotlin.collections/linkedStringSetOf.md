

# linkedStringSetOf

Creates a new instance of the specialized implementation of LinkedHashSet with the specified String elements, which elements the keys as properties of JS object without hashing them.

```kotlin
fun linkedStringSetOf(vararg elements: String): LinkedHashSet<String>(source)
```

```kotlin
val fruits = linkedStringSetOf("apple", "banana", "cherry")

// Add a new fruit
fruits.add("date")

// Remove a fruit
fruits.remove("banana")

// Iterate and print each fruit
for (fruit in fruits) {
    println(fruit)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/linked-string-set-of.html)

    