

# lastIndexOf

Returns last index of element, or -1 if the sequence does not contain element.

```kotlin
fun <T> Sequence<T>.lastIndexOf(element: T): Int(source)
```

```kotlin
fun main() {
    val seq = sequenceOf("apple", "banana", "cherry", "banana")
    val index = seq.lastIndexOf("banana")
    println("Last index of 'banana' is $index") // prints: Last index of 'banana' is 3
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/last-index-of.html)

    