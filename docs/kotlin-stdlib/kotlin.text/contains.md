

# contains

Returns true if this char sequence contains the specified other sequence of characters as a substring.

```kotlin
operator fun CharSequence.contains(other: CharSequence, ignoreCase: Boolean = false): Boolean(source)
```

```kotlin
val text = "Hello, Kotlin!"

// Case-sensitive check
val containsKotlin = text.contains("kotlin")   // false

// Case-insensitive check
val containsKotlinIgnoreCase = text.contains("kotlin", ignoreCase = true) // true

println("containsKotlin: $containsKotlin")
println("containsKotlinIgnoreCase: $containsKotlinIgnoreCase")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/contains.html)

    