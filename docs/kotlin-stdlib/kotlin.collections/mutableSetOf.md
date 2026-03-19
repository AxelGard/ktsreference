

# mutableSetOf

Returns an empty new MutableSet.

```kotlin
inline fun <T> mutableSetOf(): MutableSet<T>(source)
```

```kotlin
val fruits = mutableSetOf("apple", "banana", "cherry")

// Add a new element
fruits.add("date")

// Remove an element
fruits.remove("banana")

// Iterate over the set
for (fruit in fruits) {
    println(fruit)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/mutable-set-of.html)

    