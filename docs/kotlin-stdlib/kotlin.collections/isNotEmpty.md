

# isNotEmpty

Returns true if the array is not empty.

```kotlin
inline fun <T> Array<out T>.isNotEmpty(): Boolean(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3)

if (numbers.isNotEmpty()) {
    println("The array has ${numbers.size} elements.")
} else {
    println("The array is empty.")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/is-not-empty.html)

    