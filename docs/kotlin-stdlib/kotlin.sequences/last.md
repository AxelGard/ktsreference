

# last

Returns the last element.

```kotlin
fun <T> Sequence<T>.last(): T(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(10, 20, 30, 40, 50)
    val lastNumber = numbers.last()
    println("Last number: $lastNumber")   // Output: Last number: 50
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/last.html)

    