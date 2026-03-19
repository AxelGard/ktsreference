

# reverse

Reverses elements in the array in-place.

```kotlin
fun <T> Array<T>.reverse()(source)
```

fun main() {
    val fruits = arrayOf("apple", "banana", "cherry")
    println("Original: ${fruits.contentToString()}")
    fruits.reverse()
    println("Reversed: ${fruits.contentToString()}")
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/reverse.html)

    