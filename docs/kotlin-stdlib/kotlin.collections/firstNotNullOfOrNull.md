

# firstNotNullOfOrNull

Returns the first non-null value produced by transform function being applied to elements of this array in iteration order, or null if no non-null value was produced.

```kotlin
inline fun <T, R : Any> Array<out T>.firstNotNullOfOrNull(transform: (T) -> R?): R?(source)
```

```kotlin
data class User(val id: Int, val name: String?)

fun main() {
    val users = arrayOf(
        User(1, null),
        User(2, "Alice"),
        User(3, "Bob")
    )

    val firstNonNullName = users.firstNotNullOfOrNull { it.name }
    println(firstNonNullName)   // Prints: Alice
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/first-not-null-of-or-null.html)

    