

# indices

Returns the range of valid indices for the array.

```kotlin
val <T> Array<out T>.indices: IntRange(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("Apple", "Banana", "Cherry")
    for (i in fruits.indices) {
        println("Index $i: ${fruits[i]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/indices.html)

    