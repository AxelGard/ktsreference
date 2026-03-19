

# component1

Returns 1st element from the array.

```kotlin
inline operator fun <T> Array<out T>.component1(): T(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3)
    val first = numbers.component1()
    println(first) // Output: 1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/component1.html)

    