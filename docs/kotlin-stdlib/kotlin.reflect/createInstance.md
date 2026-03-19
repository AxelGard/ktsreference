

# createInstance

Creates a new instance of the class, calling a constructor which either has no parameters or all parameters of which have a default value. If there are no or many such constructors, an exception is thrown.

```kotlin
@ExperimentalJsReflectionCreateInstancefun <T : Any> KClass<T>.createInstance(): T(source)
```

```kotlin
import kotlin.reflect.full.createInstance
import kotlin.reflect.jvm.ExperimentalJsReflectionCreateInstance

@OptIn(ExperimentalJsReflectionCreateInstance::class)
fun main() {
    data class Person(val name: String = "Alice", val age: Int = 28)

    // Create an instance using the no‑arg/default constructor via reflection
    val person = Person::class.createInstance()

    println(person)  // Output: Person(name=Alice, age=28)
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.reflect/create-instance.html)

    