

# toCollection

Appends all elements to the given destination collection.

```kotlin
@IgnorableReturnValuefun <T, C : MutableCollection<in T>> Sequence<T>.toCollection(destination: C): C(source)
```

```kotlin
fun main() {
    val seq = sequenceOf("kotlin", "java", "c++")
    val list = mutableListOf<String>()
    seq.toCollection(list)
    println(list) // [kotlin, java, c++]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/to-collection.html)

    