

# associateWith

Returns a Map where keys are elements from the given array and values are produced by the valueSelector function applied to each element.

```kotlin
inline fun <K, V> Array<out K>.associateWith(valueSelector: (K) -> V): Map<K, V>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4)
    val squares = numbers.associateWith { it * it }
    println(squares) // prints {1=1, 2=4, 3=9, 4=16}
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/associate-with.html)

    