

# minusElement

Returns a sequence containing all elements of the original sequence without the first occurrence of the given element.

```kotlin
inline fun <T> Sequence<T>.minusElement(element: T): Sequence<T>(source)
```

```kotlin
fun main() {
    val numbers = sequenceOf(1, 2, 3, 2, 4, 5)
    val withoutFirstTwo = numbers.minusElement(2)

    // Convert to a list to see the result
    println(withoutFirstTwo.toList()) // Output: [1, 3, 2, 4, 5]
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/minus-element.html)

    