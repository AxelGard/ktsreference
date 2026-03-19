

# plusElement

Returns a sequence containing all elements of the original sequence and then the given element.

```kotlin
inline fun <T> Sequence<T>.plusElement(element: T): Sequence<T>(source)
```

```kotlin
val original = sequenceOf("a", "b", "c")
val extended = original.plusElement("d")
println(extended.toList()) // [a, b, c, d]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/plus-element.html)

    